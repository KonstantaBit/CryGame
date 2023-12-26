from perlin_noise import PerlinNoise
from .block import Block
from src.BlockType import *
from constants import CHUNK_SIZE, TEXTURE_SIZE


class Chunk:
    def __init__(self):
        self.blocks: list[list[Block]] = [[None] * CHUNK_SIZE for _ in range(CHUNK_SIZE)]

    def generate(self, x, y, seed):
        perlin_noise_height = PerlinNoise(seed=seed, octaves=2,)
        perlin_noise_ores = PerlinNoise(seed=seed + 100, octaves=5, )
        for i in range(CHUNK_SIZE):
            for j in range(CHUNK_SIZE):
                height = perlin_noise_height([(x * CHUNK_SIZE + i) / 1024, (y * CHUNK_SIZE + j) / 1024])
                ore_rating = perlin_noise_ores([(x * CHUNK_SIZE + i) / 256, (y * CHUNK_SIZE + j) / 256])
                temp = Block()
                if height < -0.015:
                    temp.set_type(Water())
                elif height < -0.01:
                    temp.set_type(Sand())
                else:
                    temp.set_type(Grass())
                    print((255 - 100, 255 - (200 * abs(ore_rating)), 255 - 100))
                    temp.block_type.texture.fill((255 - 100, 255 - (200 * (1 - abs(height))), 255 - 100) + (0,), None, pg.BLEND_RGBA_SUB)
                if ore_rating * 3 > 0.5:
                    temp.contain.append("Iron")
                    temp.set_type(Dirt())
                temp.contain.append(ore_rating * 2)
                self.blocks[i][j] = temp

    @property
    def texture(self) -> pg.Surface:
        surface = pg.Surface((CHUNK_SIZE * TEXTURE_SIZE, CHUNK_SIZE * TEXTURE_SIZE))
        for i in range(CHUNK_SIZE):
            for j in range(CHUNK_SIZE):
                surface.blit(self.blocks[i][j].texture, (TEXTURE_SIZE * i, TEXTURE_SIZE * j))
        return surface
