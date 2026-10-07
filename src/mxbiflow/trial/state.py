from math import isfinite

from .actions import Action
from .events import SemanticEvent


class State:
    """Mutable declarative definition of one trial state.

    Durations are milliseconds. ``None`` means that the state has no timeout;
    zero means that its timeout transition is immediate.
    """

    def __init__(self, name: str) -> None:
        if not name.strip():
            raise ValueError("state name must not be empty")
        self.name = name
        self._duration: float | None = 0.0
        self.on_entry: list[Action] = []
        self.on_exit: list[Action] = []
        self.wait_events: list[SemanticEvent] = []
        self.next_state_after_event: dict[SemanticEvent, str | None] = {}
        self.next_state_after_timeout: str | None = None

    @property
    def duration(self) -> float | None:
        return self._duration

    @duration.setter
    def duration(self, value: float | None) -> None:
        if value is None:
            self._duration = None
            return
        if isinstance(value, bool) or not isfinite(value) or value < 0:
            raise ValueError(
                "state duration must be a finite non-negative number or None"
            )
        self._duration = float(value)

    def __repr__(self) -> str:
        return f"State({self.name!r})"
