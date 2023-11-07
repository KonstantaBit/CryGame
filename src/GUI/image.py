import pygame as pg
from src.CryGame.scene_object import SceneObjectInterface


class Image(SceneObjectInterface):
    def __init__(self, image_ref: str, x: int, y: int):
        self.image = pg.image.load(image_ref).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, display: pg.Surface):
        display.blit(self.image, self.rect.topleft)
