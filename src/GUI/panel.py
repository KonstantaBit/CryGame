import pygame as pg

from .movable_object import MovableGUIObject


class Panel(MovableGUIObject):
    def __init__(self, rect: pg.Rect, transparency: int, color: pg.Color):
        super().__init__(rect)
        self.rect = rect
        self.color = color
        self.transparency = transparency
        self.surface = self._make_surface()

    def move(self, x: int, y: int) -> None:
        self.rect.topleft = x, y
        self.surface = self._make_surface()

    def resize(self, width: int, height: int) -> None:
        self.rect.width = width
        self.rect.height = height
        self.surface = self._make_surface()

    def _make_surface(self) -> pg.Surface:
        surface = pg.Surface(self.rect.size)
        surface.set_alpha(self.transparency)
        return surface

    def draw(self, display: pg.Surface):
        self.surface.fill(self.color)
        display.blit(self.surface, self.rect.topleft)
