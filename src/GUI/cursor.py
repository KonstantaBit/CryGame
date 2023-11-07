import pygame as pg
from src.CryGame.scene_object import SceneObjectInterface


class Cursor(SceneObjectInterface):
    def __init__(self, imageref):
        pg.mouse.set_visible(False)
        self.image = pg.image.load(imageref).convert_alpha()
        
    def draw(self, surface: pg.Surface):
        surface.blit(self.image, pg.mouse.get_pos())
