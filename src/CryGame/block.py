from src.BlockType import BaseBlockType
import pygame as pg


class Block:
    def __init__(self):
        self.block_type: BaseBlockType = None
        self.contain: list = list()

    def set_type(self, block_type: BaseBlockType):
        self.block_type: BaseBlockType = block_type

    @property
    def texture(self):
        return self.block_type.texture
