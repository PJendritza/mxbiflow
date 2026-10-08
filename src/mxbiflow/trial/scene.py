from collections.abc import Callable
from dataclasses import dataclass
from time import time
from typing import ClassVar

import pygame
from pygame.event import Event
from pygame.surface import Surface

from mxbiflow.core.context import MXBIFlow, get_mxbiflow
from mxbiflow.scene import Scene

from .events import TouchSample
from .runtime import TrialRuntime
from .trial import Trial


@dataclass(frozen=True, slots=True)
class TrialSceneContext:
    mxbiflow: MXBIFlow
    scene_name: str


type TrialFactory = Callable[[TrialSceneContext], Trial]


class TrialScene(Scene):
    """Scene adapter that runs one declarative :class:`Trial` instance."""

    level_table: ClassVar[dict[str, list[int]]] = {}
    trial_factory: ClassVar[TrialFactory | None] = None

    def __init__(self) -> None:
        super().__init__()
        self._mxbiflow = get_mxbiflow()
        self._trial: Trial | None = None
        self._runtime: TrialRuntime | None = None
        self._started = False
        self._finalized = False

    @property
    def trial(self) -> Trial | None:
        return self._trial

    @property
    def runtime(self) -> TrialRuntime | None:
        return self._runtime

    def start(self) -> None:
        if self._started:
            raise RuntimeError("trial scene has already started")
        factory = type(self).trial_factory
        if factory is None:
            raise RuntimeError(f"{type(self).__name__}.trial_factory is not configured")

        self._started = True
        self._mxbiflow.session.add_trial()
        context = TrialSceneContext(self._mxbiflow, self.name())
        trial = factory(context)
        self._trial = trial
        self._runtime = TrialRuntime(trial)
        self._running = True
        self._runtime.start()
        if self._runtime.completed:
            self.quit()

    def quit(self) -> None:
        if self._finalized:
            return
        self._finalized = True

        completed = self._runtime.completed if self._runtime is not None else False
        try:
            if self._runtime is not None and not self._runtime.completed:
                self._runtime.stop()
            if self._trial is not None:
                for callback in self._trial.finish_callbacks:
                    callback(completed)
        finally:
            self._mxbiflow.mxbi.aplayer.cancel_all()
            self._running = False

    def handle_event(self, event: Event) -> None:
        if not self._running:
            return
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self._handle_touch((int(event.pos[0]), int(event.pos[1])))
        elif event.type == pygame.FINGERDOWN:
            screen = self._mxbiflow.mxbi.screen_size
            self._handle_touch(
                (int(event.x * screen.width), int(event.y * screen.height))
            )

    def update(self, dt_s: float) -> None:
        if not self._running or self._runtime is None:
            return
        if self._trial is not None:
            for stimulus in self._trial.stimuli:
                stimulus.update(dt_s)
        self._runtime.update(dt_s)
        if self._runtime.completed:
            self.quit()

    def draw(self, screen: Surface) -> None:
        if self._trial is None:
            return
        for stimulus in self._trial.stimuli:
            stimulus.draw(screen)

    def _handle_touch(self, position: tuple[int, int]) -> None:
        if self._trial is None or self._runtime is None:
            return
        sample = TouchSample(position[0], position[1], time())
        for observer in self._trial.touch_observers:
            observer(sample)

        for tracker in self._trial.touch_trackers:
            semantic_event = tracker.event_at(position)
            if semantic_event is not None:
                self._runtime.emit(semantic_event, sample)
                return

        if self._trial.unclaimed_touch_event is not None:
            self._runtime.emit(self._trial.unclaimed_touch_event, sample)
