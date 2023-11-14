from abc import ABC, abstractmethod

import pygame as pg

from .base_object import BaseGUIObject


class MovableGUIObject(BaseGUIObject, ABC):
    def __init__(self, rect: pg.Rect):
        self.rect: pg.Rect = pg.Rect(rect)

    @abstractmethod
    def move(self, x: int, y: int) -> None:
        pass

    @abstractmethod
    def resize(self, width: int, height: int) -> None:
        pass
