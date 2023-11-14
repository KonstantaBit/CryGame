import pygame as pg

from .movable_object import MovableGUIObject


class Text(MovableGUIObject):
    def __init__(self, rect: pg.Rect, text: str, size: int, color: pg.Color, font: str):
        super().__init__(rect)
        self.text = text
        self.rect = rect
        self.size = size
        self.color = color
        self.font = font
        self._config_font()
        self._config_text()

    def _config_font(self):
        try:
            self.graphic_font = pg.font.Font(self.font, self.size)
        except OSError:  # can't read font file.
            self.graphic_font = pg.font.SysFont(self.font, self.size)

    def _config_text(self):
        self.graphic_text = self.graphic_font.render(self.text, True, self.color)
        self.rect.size = self.graphic_text.get_rect().size

    def change_text(self, text: str) -> None:
        self.text = text
        self._config_text()

    def move(self, x: int, y: int) -> None:
        self.rect.topleft = x, y

    def resize(self, width: int, height: int) -> None:
        pass

    def draw(self, display):
        display.blit(self.graphic_text, self.rect.topleft)
