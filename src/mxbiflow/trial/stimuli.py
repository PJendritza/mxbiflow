from abc import ABC, abstractmethod
from collections import deque
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from time import monotonic
from typing import Protocol

import pygame
from pygame.surface import Surface
from pygame.typing import ColorLike

from mxbiflow.assets import ImageSprite, create_background


class Stimulus(ABC):
    """Experiment-facing drawable with optional hit testing."""

    def __init__(self, *, visible: bool = True) -> None:
        self.visible = visible

    @abstractmethod
    def draw(self, screen: Surface) -> None: ...

    def update(self, dt_s: float) -> None:
        """Advance a dynamic stimulus without blocking the scene loop."""

        del dt_s

    def contains(self, position: tuple[int, int]) -> bool:
        del position
        return False


class Background(Stimulus):
    def __init__(
        self,
        screen_size: tuple[int, int],
        *,
        border_width: int = 40,
        border_color: ColorLike = (255, 255, 255),
        background_color: ColorLike = (0, 0, 0),
        visible: bool = True,
    ) -> None:
        super().__init__(visible=visible)
        self._surface = create_background(
            screen_size,
            border_width=border_width,
            border_color=border_color,
            background_color=background_color,
        )

    def draw(self, screen: Surface) -> None:
        if self.visible:
            screen.blit(self._surface, (0, 0))


class Image(Stimulus):
    def __init__(
        self,
        path: Path,
        *,
        size: int | None = None,
        position: tuple[int, int] = (0, 0),
        visible: bool = True,
    ) -> None:
        super().__init__(visible=visible)
        self._sprite = ImageSprite(path, size, position)
        image = self._sprite.image
        rect = self._sprite.rect
        if image is None or rect is None:
            raise RuntimeError("image stimulus failed to initialize")
        self._image = image
        self._rect = rect

    @property
    def position(self) -> tuple[int, int]:
        return (int(self._rect.centerx), int(self._rect.centery))

    @position.setter
    def position(self, value: tuple[int, int]) -> None:
        self._rect.center = value

    def draw(self, screen: Surface) -> None:
        if self.visible:
            screen.blit(self._image, self._rect)

    def contains(self, position: tuple[int, int]) -> bool:
        return self.visible and self._rect.collidepoint(position)


class TimestampedPosition(Protocol):
    """Minimal sample shape consumed by :class:`PositionTrail`."""

    @property
    def timestamp_ns(self) -> int: ...

    @property
    def x(self) -> float: ...

    @property
    def y(self) -> float: ...


type PositionProvider = Callable[[], TimestampedPosition | None]
type RGBColor = tuple[int, int, int]


@dataclass(frozen=True, slots=True)
class _TrailPoint:
    received_at_s: float
    position: tuple[int, int]


class PositionTrail(Stimulus):
    """Draw the latest sampled position and a time-faded history."""

    def __init__(
        self,
        position_provider: PositionProvider,
        *,
        history_ms: int = 400,
        trail_radius_px: int = 4,
        current_radius_px: int = 8,
        trail_min_alpha: int = 20,
        trail_max_alpha: int = 170,
        dot_color: RGBColor = (255, 40, 40),
        visible: bool = True,
    ) -> None:
        super().__init__(visible=visible)
        if history_ms <= 0:
            raise ValueError("history_ms must be positive")
        if trail_radius_px <= 0 or current_radius_px <= 0:
            raise ValueError("trail radii must be positive")
        if not 0 <= trail_min_alpha <= trail_max_alpha <= 255:
            raise ValueError("trail alpha values must satisfy 0 <= min <= max <= 255")

        self._position_provider = position_provider
        self._history_ms = history_ms
        self._trail_radius_px = trail_radius_px
        self._current_radius_px = current_radius_px
        self._trail_min_alpha = trail_min_alpha
        self._trail_max_alpha = trail_max_alpha
        self._dot_color = dot_color
        self._history: deque[_TrailPoint] = deque()
        self._current_position: tuple[int, int] | None = None
        self._last_sample_timestamp_ns: int | None = None

    def update(self, dt_s: float) -> None:
        del dt_s
        now = monotonic()
        sample = self._position_provider()

        if sample is None:
            self._current_position = None
        else:
            position = (round(sample.x), round(sample.y))
            self._current_position = position
            if sample.timestamp_ns != self._last_sample_timestamp_ns:
                self._history.append(_TrailPoint(now, position))
                self._last_sample_timestamp_ns = sample.timestamp_ns

        oldest_allowed_s = now - self._history_ms / 1000
        while self._history and self._history[0].received_at_s < oldest_allowed_s:
            self._history.popleft()

    def draw(self, screen: Surface) -> None:
        if not self.visible:
            return

        overlay = Surface(screen.get_size(), pygame.SRCALPHA)
        now = monotonic()
        for point in self._history:
            pygame.draw.circle(
                overlay,
                (*self._dot_color, self._trail_alpha(now - point.received_at_s)),
                point.position,
                self._trail_radius_px,
            )

        if self._current_position is not None:
            radius = self._current_radius_px
            pygame.draw.circle(
                overlay,
                (*self._dot_color, 35),
                self._current_position,
                radius * 2,
            )
            pygame.draw.circle(
                overlay,
                (*self._dot_color, 100),
                self._current_position,
                radius + 3,
            )
            pygame.draw.circle(
                overlay,
                (*self._dot_color, 255),
                self._current_position,
                radius,
            )

        screen.blit(overlay, (0, 0))

    def _trail_alpha(self, age_s: float) -> int:
        age_fraction = min(1.0, max(0.0, age_s * 1000 / self._history_ms))
        alpha_range = self._trail_max_alpha - self._trail_min_alpha
        return round(self._trail_max_alpha - age_fraction * alpha_range)
