from collections.abc import Sequence

from .actions import Action
from .events import EventQueue, SemanticEvent
from .state import State
from .trial import Trial


class TrialRuntime:
    """Nonblocking state-machine executor driven by frame delta time."""

    def __init__(
        self,
        trial: Trial,
        *,
        max_immediate_transitions: int = 100,
    ) -> None:
        if max_immediate_transitions < 1:
            raise ValueError("max_immediate_transitions must be at least 1")
        self.trial = trial
        self.events = EventQueue()
        self.max_immediate_transitions = max_immediate_transitions
        self.current_state: State | None = None
        self.state_elapsed_ms = 0.0
        self.started = False
        self.completed = False

    def start(self) -> None:
        if self.started:
            raise RuntimeError("trial runtime has already started")
        self.started = True
        self.events.clear()
        self._enter(self.trial.states[self.trial.initial_state])
        self._drain_immediate_transitions()

    def emit(self, event: SemanticEvent, payload: object | None = None) -> None:
        if self.completed:
            return
        self.events.emit(event, payload)

    def update(self, dt_s: float) -> None:
        if not self.started:
            raise RuntimeError("trial runtime has not started")
        if dt_s < 0:
            raise ValueError("dt_s must not be negative")
        if self.completed:
            self.events.clear()
            return

        self.state_elapsed_ms += dt_s * 1000.0
        state = self._require_current_state()

        records = self.events.drain()
        for record in records:
            if record.event in state.wait_events:
                self._transition(state.next_state_after_event[record.event])
                self._drain_immediate_transitions()
                return

        duration = state.duration
        if duration is not None and self.state_elapsed_ms >= duration:
            self._transition(state.next_state_after_timeout)
            self._drain_immediate_transitions()

    def stop(self) -> None:
        """Stop an unfinished trial, executing the active state's exit actions."""

        if self.completed:
            return
        if self.current_state is not None:
            self._execute(self.current_state.on_exit)
        self.current_state = None
        self.completed = True
        self.events.clear()

    def _enter(self, state: State) -> None:
        self.current_state = state
        self.state_elapsed_ms = 0.0
        self._execute(state.on_entry)

    def _transition(self, target: str | None) -> None:
        state = self._require_current_state()
        self._execute(state.on_exit)
        self.events.clear()
        if target is None:
            self.current_state = None
            self.completed = True
            return
        try:
            next_state = self.trial.states[target]
        except KeyError as error:
            raise RuntimeError(f"next state does not exist: {target}") from error
        self._enter(next_state)

    def _drain_immediate_transitions(self) -> None:
        count = 0
        while not self.completed:
            state = self._require_current_state()
            if state.duration != 0:
                return
            if count >= self.max_immediate_transitions:
                raise RuntimeError(
                    "immediate transition limit exceeded; check for a zero-duration cycle"
                )
            count += 1
            self._transition(state.next_state_after_timeout)

    def _execute(self, actions: Sequence[Action]) -> None:
        for action in actions:
            action.execute(self.trial.context)

    def _require_current_state(self) -> State:
        if self.current_state is None:
            raise RuntimeError("trial has no current state")
        return self.current_state
