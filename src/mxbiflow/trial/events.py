from collections import deque
from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True, slots=True)
class SemanticEvent:
    """An input-source-independent event consumed by trial states."""

    name: str

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("event name must not be empty")

    def __str__(self) -> str:
        return self.name


@dataclass(frozen=True, slots=True)
class EventRecord:
    event: SemanticEvent
    payload: object | None
    sequence: int


class EventQueue:
    """FIFO queue for semantic events emitted between runtime updates."""

    def __init__(self) -> None:
        self._records: deque[EventRecord] = deque()
        self._next_sequence = 0

    def emit(self, event: SemanticEvent, payload: object | None = None) -> None:
        self._records.append(EventRecord(event, payload, self._next_sequence))
        self._next_sequence += 1

    def drain(self) -> tuple[EventRecord, ...]:
        records = tuple(self._records)
        self._records.clear()
        return records

    def clear(self) -> None:
        self._records.clear()

    def __len__(self) -> int:
        return len(self._records)


@dataclass(frozen=True, slots=True)
class TouchSample:
    x: int
    y: int
    timestamp: float

    @property
    def position(self) -> tuple[int, int]:
        return (self.x, self.y)


class TouchRegion(Protocol):
    def contains(self, position: tuple[int, int]) -> bool: ...


@dataclass(frozen=True, slots=True)
class TouchTracker:
    region: TouchRegion
    event: SemanticEvent

    def event_at(self, position: tuple[int, int]) -> SemanticEvent | None:
        return self.event if self.region.contains(position) else None


@dataclass(frozen=True, slots=True)
class TouchEvents:
    """Semantic events and tracker produced for a touch region."""

    touched: SemanticEvent
    tracker: TouchTracker


def track_touch(region: TouchRegion, name: str) -> TouchEvents:
    """Create a semantic ``<name>Touched`` event for a hit-testable region."""

    event = SemanticEvent(f"{name}Touched")
    return TouchEvents(touched=event, tracker=TouchTracker(region, event))
