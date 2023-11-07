import pygame as pg
from src.CryGame.scene_object import SceneObjectInterface


class Panel(SceneObjectInterface):
    def __init__(self, rect, transparency, colour):
        self.rect = pg.Rect(rect)
        self.colour = colour
        self.transparency = transparency
        self.surface = self.make_surface()

    def reset_rect(self, rect):
        self.rect = pg.Rect(rect)
        self.surface = self.make_surface()

    def reset_width(self, width):
        self.rect.width = width
        self.surface = self.make_surface()

    def make_surface(self):
        surface = pg.Surface([self.rect[2], self.rect[3]])
        surface.set_alpha(self.transparency)
        return surface

    def draw(self, display: pg.Surface):
        self.surface.fill(self.colour)
        display.blit(self.surface, [self.rect[0], self.rect[1]])
