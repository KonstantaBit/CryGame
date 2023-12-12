from abc import ABC
import pygame as pg
from paths import tiles_path
import os


class BaseBlockType(ABC):
    def __init__(self):
        self.name: str = None
        self.texture: pg.Surface = None


class Clay(BaseBlockType):
    def __init__(self):
        super().__init__()
        self.name: str = 'Глина'
        self.texture: pg.Surface = pg.image.load(os.path.join(tiles_path, 'clay.png')).convert_alpha()


class Dirt(BaseBlockType):
    def __init__(self):
        super().__init__()
        self.name: str = 'Земля'
        self.texture: pg.Surface = pg.image.load(os.path.join(tiles_path, 'dirt.png')).convert_alpha()


class Grass(BaseBlockType):
    def __init__(self):
        super().__init__()
        self.name: str = 'Трава'
        self.texture: pg.Surface = pg.image.load(os.path.join(tiles_path, 'grass.png')).convert_alpha()


class Gravel(BaseBlockType):
    def __init__(self):
        super().__init__()
        self.name: str = 'Гравий'
        self.texture: pg.Surface = pg.image.load(os.path.join(tiles_path, 'gravel.png')).convert_alpha()


class Sand(BaseBlockType):
    def __init__(self):
        super().__init__()
        self.name: str = 'Песок'
        self.texture: pg.Surface = pg.image.load(os.path.join(tiles_path, 'sand.png')).convert_alpha()


class Stone(BaseBlockType):
    def __init__(self):
        super().__init__()
        self.name: str = 'Камень'
        self.texture: pg.Surface = pg.image.load(os.path.join(tiles_path, 'stone.png')).convert_alpha()


class Water(BaseBlockType):
    def __init__(self):
        super().__init__()
        self.name: str = 'Вода'
        self.texture: pg.Surface = pg.image.load(os.path.join(tiles_path, 'blue_wool.png')).convert_alpha()