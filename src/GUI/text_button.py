import pygame as pg

from .text import Text
from .panel import Panel
from .clickable_object import ClickableGUIObject


class TextButton(ClickableGUIObject):
    def __init__(self, rect: pg.Rect, start_transparency: int, hover_transparancy: int,
                 text: str, text_size: int, text_color: pg.Color, text_font: str):
        super().__init__(rect)

        self.text = Text(rect, text, text_size, text_color, text_font)
        # Moving text to center in button
        padding_x = (self.rect.width - self.text.rect.width) / 2
        padding_y = (self.rect.height - self.text.rect.height) / 2
        self.text.rect.x += padding_x
        self.text.rect.y += padding_y

        self.panel = Panel(self.rect, start_transparency, pg.Color(0, 0, 0))
        self.hover_panel = Panel(self.rect, hover_transparancy, pg.Color(0, 0, 0))

    def move(self, x: int, y: int) -> None:
        self.rect.topleft = x, y
        self.text.move(x, y)
        # Moving text to center in button
        padding_x = (self.rect.width - self.text.rect.width) / 2
        padding_y = (self.rect.height - self.text.rect.height) / 2
        self.text.rect.x += padding_x
        self.text.rect.y += padding_y
        self.panel.move(x, y)
        self.hover_panel.move(x, y)

    def resize(self, width: int, height: int) -> None:
        self.rect.size = width, height
        self.text.rect.topleft = self.rect.topleft
        # Moving text to center in button
        padding_x = (self.rect.width - self.text.rect.width) / 2
        padding_y = (self.rect.height - self.text.rect.height) / 2
        self.text.rect.x += padding_x
        self.text.rect.y += padding_y
        self.panel.resize(width, height)
        self.hover_panel.resize(width, height)

    def draw(self, display):
        if self.mouse_over():
            self.hover_panel.draw(display)
        else:
            self.panel.draw(display)
        self.text.draw(display)
