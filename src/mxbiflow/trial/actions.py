from abc import ABC, abstractmethod
from collections.abc import Callable
from typing import Any


class Action(ABC):
    """Deferred operation executed by a trial state."""

    @abstractmethod
    def execute(self, context: object) -> None:
        """Execute the action with the trial's runtime context."""


class Set(Action):
    """Set one or more object attributes when this action is executed."""

    def __init__(self, target: object, **values: object) -> None:
        if not values:
            raise ValueError("Set requires at least one property")
        missing = [name for name in values if not hasattr(target, name)]
        if missing:
            names = ", ".join(sorted(missing))
            raise AttributeError(f"target has no attribute(s): {names}")
        self._target = target
        self._values = dict(values)

    def execute(self, context: object) -> None:
        del context
        for name, value in self._values.items():
            setattr(self._target, name, value)


class Call(Action):
    """Defer a regular callable without wrapping it in a lambda."""

    def __init__(
        self,
        callback: Callable[..., None],
        /,
        *args: object,
        **kwargs: object,
    ) -> None:
        self._callback = callback
        self._args = args
        self._kwargs: dict[str, Any] = kwargs

    def execute(self, context: object) -> None:
        del context
        self._callback(*self._args, **self._kwargs)
