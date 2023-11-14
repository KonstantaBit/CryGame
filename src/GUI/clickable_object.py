from abc import ABC

import pygame as pg

from .movable_object import MovableGUIObject


class ClickableGUIObject(MovableGUIObject, ABC):
    def mouse_over(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            return True
        return False
