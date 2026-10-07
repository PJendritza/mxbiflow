from abc import ABC, abstractmethod
from pathlib import Path

from pygame.surface import Surface
from pygame.typing import ColorLike

from mxbiflow.assets import ImageSprite, create_background


class Stimulus(ABC):
    """Experiment-facing drawable with optional hit testing."""

    def __init__(self, *, visible: bool = True) -> None:
        self.visible = visible

    @abstractmethod
    def draw(self, screen: Surface) -> None: ...

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
