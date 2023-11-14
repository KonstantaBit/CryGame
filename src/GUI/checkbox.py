import pygame as pg

from .image import Image
from .clickable_object import ClickableGUIObject


class Checkbox(ClickableGUIObject):
    def __init__(self, rect: pg.Rect, rest_image: str, hover_image: str, active_image: str, active_hover_image: str):
        super().__init__(rect)
        self.rest_image = Image(rect, rest_image)
        self.hover_image = Image(rect, hover_image)
        self.active_image = Image(rect, active_image)
        self.active_hover_image = Image(rect, active_hover_image)
        self.rect.size = self.rest_image.image.get_rect().size
        self.active = False

    def move(self, x: int, y: int) -> None:
        self.rest_image.move(x, y)
        self.hover_image.move(x, y)
        self.active_image.move(x, y)
        self.active_hover_image.move(x, y)
        self.rect.topleft = x, y

    def resize(self, width: int, height: int) -> None:
        self.rest_image.resize(width, height)
        self.hover_image.resize(width, height)
        self.active_image.resize(width, height)
        self.active_hover_image.resize(width, height)
        self.rect.size = width, height
    
    def draw(self, display: pg.Surface):
        if self.mouse_over():
            if self.active:
                self.active_hover_image.draw(display)
            else:
                self.hover_image.draw(display)
        else:
            if self.active:
                self.active_image.draw(display)
            else:
                self.rest_image.draw(display)
