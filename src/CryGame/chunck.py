from perlin_noise import PerlinNoise
from .block import Block
from src.BlockType import *


class Chunk:
    def __init__(self):
        self.blocks = [[None] * 64 for _ in range(64)]

    def get_block(self, local_x, local_y, z):
        pass

    def get_upper_block(self, local_x, local_y, z):
        pass

    def del_block(self, local_x, local_y, z):
        pass

    def generate(self, x, y, seed):
        perlin_noise_height = PerlinNoise(seed=seed, octaves=2,)
        for i in range(64):
            for j in range(64):
                value = perlin_noise_height([(x * 64 + i) / 1024, (y * 64 + j) / 1024])
                # Тут фабрику можно использовать, но потом
                temp = Block()
                if value < -0.015:
                    temp.set_type(Water())
                elif value < -0.01:
                    temp.set_type(Sand())
                else:
                    temp.set_type(Dirt())
                self.blocks[i][j] = temp
