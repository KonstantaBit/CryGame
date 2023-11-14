import pygame as pg

from .clickable_object import ClickableGUIObject
from .image import Image


class Button(ClickableGUIObject):
    def __init__(self, rect: pg.Rect, rest_image: str, hover_image: str):
        super().__init__(rect)
        self.rest_image = Image(rect, rest_image)
        self.hover_image = Image(rect, hover_image)
        self.rect.size = self.rest_image.image.get_rect().size

    def move(self, x: int, y: int) -> None:
        self.rest_image.move(x, y)
        self.hover_image.move(x, y)
        self.rect.topleft = x, y

    def resize(self, width: int, height: int) -> None:
        self.rest_image.resize(width, height)
        self.hover_image.resize(width, height)
        self.rect.size = width, height

    def draw(self, display: pg.Surface) -> None:
        if self.mouse_over():
            self.hover_image.draw(display)
        else:
            self.rest_image.draw(display)
