from perlin_noise import PerlinNoise
from .block import Block
import os
from paths import asset_path


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
        perlin_noise = PerlinNoise(seed=seed)
        for i in range(64):
            for j in range(64):
                value = perlin_noise([(x * 64 + i) / 10, (y * 64 + j) / 10])
                if value < 0:
                    self.blocks[i][j] = Block(os.path.join(asset_path, "image", "tiles", "dirt.png"))
                else:
                    self.blocks[i][j] = Block(os.path.join(asset_path, "image", "tiles", "sand.png"))