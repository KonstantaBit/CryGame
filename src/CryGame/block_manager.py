from .block import Block
from paths import tiles_path
import os
import pygame as pg


class BlockManager:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def __init__(self):
        self.block = ()
        self.textures: dict = dict()

    def load_textures(self):
        print(tiles_path)
        for el in os.listdir(tiles_path):
            self.textures[el.split('.')[0]] = pg.image.load(os.path.join(tiles_path, el)).convert_alpha()
