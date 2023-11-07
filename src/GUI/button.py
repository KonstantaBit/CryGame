import pygame as pg
import src.GUI.image
from src.CryGame.scene_object import SceneObjectInterface


class Button(SceneObjectInterface):
    def __init__(self, rest_image: str, hover_image: str, x: int, y: int):
        self.rest_image = src.GUI.Image(rest_image, x, y)
        self.hover_image = src.GUI.Image(hover_image, x, y)
        self.rect = self.rest_image.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.function = None

    def set_function(self, function):
        self.function = function

    def mouse_over(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            return True
        return False

    def right_clicked(self):
        if self.mouse_over() and pg.mouse.get_pressed(3)[1]:
            if self.function is not None:
                self.function()
            return True
        return False

    def left_clicked(self):
        if self.mouse_over() and pg.mouse.get_pressed(3)[2]:
            if self.function is not None:
                self.function()
            return True
        return False
    
    def draw(self, display: pg.Surface):
        if self.mouse_over():
            self.hover_image.draw(display)
        else:
            self.rest_image.draw(display)
