from collections.abc import Callable, Iterable

from .events import SemanticEvent, TouchSample, TouchTracker
from .state import State
from .stimuli import Stimulus

FinishCallback = Callable[[bool], None]
TouchObserver = Callable[[TouchSample], None]


class Trial:
    """Validated declarative trial definition."""

    def __init__(
        self,
        *,
        initial_state: str,
        states: Iterable[State],
        context: object | None = None,
        stimuli: Iterable[Stimulus] = (),
        touch_trackers: Iterable[TouchTracker] = (),
        unclaimed_touch_event: SemanticEvent | None = None,
        touch_observers: Iterable[TouchObserver] = (),
        finish_callbacks: Iterable[FinishCallback] = (),
    ) -> None:
        state_list = tuple(states)
        names = [state.name for state in state_list]
        duplicate_names = sorted({name for name in names if names.count(name) > 1})
        if duplicate_names:
            raise ValueError(f"duplicate state name(s): {', '.join(duplicate_names)}")

        self.states = {state.name: state for state in state_list}
        if initial_state not in self.states:
            raise ValueError(f"initial state does not exist: {initial_state}")

        self.initial_state = initial_state
        self.context = context
        self.stimuli = tuple(stimuli)
        self.touch_trackers = tuple(touch_trackers)
        self.unclaimed_touch_event = unclaimed_touch_event
        self.touch_observers = tuple(touch_observers)
        self.finish_callbacks = tuple(finish_callbacks)

        self._validate_states()

    def _validate_states(self) -> None:
        for state in self.states.values():
            for action in (*state.on_entry, *state.on_exit):
                from .actions import Action

                if not isinstance(action, Action):
                    raise TypeError(
                        f"state {state.name!r} contains a non-Action entry/exit item"
                    )

            wait_events = set(state.wait_events)
            mapped_events = set(state.next_state_after_event)
            if wait_events != mapped_events:
                raise ValueError(
                    f"state {state.name!r} must map every wait event exactly once"
                )

            targets = [state.next_state_after_timeout]
            targets.extend(state.next_state_after_event.values())
            for target in targets:
                if target is not None and target not in self.states:
                    raise ValueError(
                        f"state {state.name!r} references unknown state {target!r}"
                    )
