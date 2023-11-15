import pygame as pg

from .text import Text
from .panel import Panel
from .clickable_object import ClickableGUIObject


class TextButton(ClickableGUIObject):
    def __init__(self, rect: pg.Rect, start_transparency: int, hover_transparancy: int,
                 text: str, text_size: int, text_color: pg.Color, text_font: str):
        super().__init__(rect)

        self.text = Text(rect, text, text_size, text_color, text_font)

        self.panel = Panel(self.rect, start_transparency, pg.Color(0, 0, 0))
        self.hover_panel = Panel(self.rect, hover_transparancy, pg.Color(0, 0, 0))

    def move(self, x: int, y: int) -> None:
        self.rect.topleft = x, y
        self.text.move(x, y)

        self.panel.move(x, y)
        self.hover_panel.move(x, y)

    def resize(self, width: int, height: int) -> None:
        self.rect.size = width, height
        self.text.resize(width, height)

        self.panel.resize(width, height)
        self.hover_panel.resize(width, height)

    def draw(self, display):
        if self.mouse_over():
            self.hover_panel.draw(display)
        else:
            self.panel.draw(display)
        self.text.draw(display)
