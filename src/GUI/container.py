import pygame as pg
from abc import ABC
from .movable_object import MovableGUIObject


class Container(MovableGUIObject, ABC):
    def __init__(self, rect: pg.Rect, contain: list[[MovableGUIObject, pg.Rect]] = None, padding: int = 0):
        super().__init__(rect)
        if contain is None:
            contain = list()
        self.contain: list[[MovableGUIObject, pg.Rect]] = contain
        self.padding = padding

    def add(self, obj):
        self.contain.append(obj)

    def remove(self, ind):
        self.contain.pop(ind)
