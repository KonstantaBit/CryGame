import pygame as pg

from .base_object import BaseGUIObject


class Cursor(BaseGUIObject):
    def __init__(self, image: str):
        pg.mouse.set_visible(False)
        self.image = pg.image.load(image).convert_alpha()
        
    def draw(self, surface: pg.Surface):
        surface.blit(self.image, pg.mouse.get_pos())
