from src.BlockType import BaseBlockType
import pygame as pg


class Block:
    def __init__(self):
        self.block_type: BaseBlockType = None
        self.contain = dict()
        self.texture: pg.Surface = None

    def set_type(self, block_type: BaseBlockType):
        self.block_type: BaseBlockType = block_type
        self.texture = self.block_type.texture
