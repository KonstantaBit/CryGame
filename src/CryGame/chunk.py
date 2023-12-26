from perlin_noise import PerlinNoise
from .block import Block
from src.BlockType import *
from src.Entity import *
from constants import CHUNK_SIZE, TEXTURE_SIZE


class Chunk:
    def __init__(self):
        self.blocks: list[list[Block]] = [[None] * CHUNK_SIZE for _ in range(CHUNK_SIZE)]
        self.entities: list[Entity] = list()

    def generate(self, x, y, seed):
        perlin_noise_height = PerlinNoise(seed=seed, octaves=2,)
        perlin_noise_ores = PerlinNoise(seed=seed + 1234567890, octaves=5,)
        for i in range(CHUNK_SIZE):
            for j in range(CHUNK_SIZE):
                height = perlin_noise_height([(x * CHUNK_SIZE + i) / 512, (y * CHUNK_SIZE + j) / 512])
                ore_rating = perlin_noise_ores([(x * CHUNK_SIZE + i) / 256, (y * CHUNK_SIZE + j) / 256])
                temp = Block()
                if height < -0.015:
                    temp.set_type(Water())
                elif height < -0.01:
                    temp.set_type(Sand())
                else:
                    temp.set_type(Grass())
                    temp.block_type.texture.fill((255 - 100, 255 - max(150, 200 * (1 - abs(height) * 2)), 255 - 100) + (0,), None, pg.BLEND_RGBA_SUB)
                    if height > 0.1 and random.randint(1, 3) == 1:
                        self.entities.append(Tree(Pos(x * CHUNK_SIZE + i, y * CHUNK_SIZE + j)))
                    if ore_rating * 3 > 0.5:
                        temp.contain.append("Iron")
                        temp.set_type(Gravel())
                temp.contain.append(ore_rating * 2)
                self.blocks[i][j] = temp

    @property
    def texture(self) -> pg.Surface:
        surface = pg.Surface((CHUNK_SIZE * TEXTURE_SIZE, CHUNK_SIZE * TEXTURE_SIZE))
        for i in range(CHUNK_SIZE):
            for j in range(CHUNK_SIZE):
                surface.blit(self.blocks[i][j].texture, (TEXTURE_SIZE * i, TEXTURE_SIZE * j))
        return surface
