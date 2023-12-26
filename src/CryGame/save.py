import os
import pickle
import random
from src.Entity import *
from .chunk import Chunk
from paths import saves_path
from constants import CHUNK_SIZE, RENDER_DISTANCE


class Save:
    def __init__(self, name):
        self.name = name
        self.seed = None
        self.chunks = dict()
        self.players: list[Entity] = list()
        self.entities: list[Entity] = list()

    def update(self):
        for el in self.players:
            el.update()
        for el in self.entities:
            el.update()

    def load_chunk(self, x: int, y: int):
        try:
            with open(os.path.join(saves_path, self.name, "chunks", f"x{x}y{y}.dat"), "rb") as file:
                self.chunks[(x, y)] = pickle.load(file)
        except FileNotFoundError as error:
            #  Потом нужно будет сделать проверку, что чанк впервые генерируется.
            #  Сейчас можно просто файл удалить и чанк перегенерируется
            temp_chunk = Chunk()
            temp_chunk.generate(x, y, self.seed)
            self.chunks[(x, y)] = temp_chunk
        finally:
            self.entities.extend(self.chunks[(x, y)].entities)

    def save_chunk(self, x: int, y: int):
        with open(os.path.join(saves_path, self.name, "chunks", f"x{x}y{y}.dat"), "wb") as file:
            pickle.dump(self.chunks[(x, y)], file)
        del self.chunks[(x, y)]

    def save_all_chunks(self):
        for el in self.chunks.keys():
            self.save_chunk(*el)
        self.chunks.clear()

    def manage_chunks(self, load_points: list[[int, int]]):
        for el in load_points:
            for i in range(-RENDER_DISTANCE, RENDER_DISTANCE + 1):
                for j in range(-RENDER_DISTANCE, RENDER_DISTANCE + 1):
                    if (el[0] + i, el[1] + j) not in self.chunks.keys():
                        self.load_chunk(el[0] + i, el[1] + j)

    @staticmethod
    def get_chunk_number_by_cords(x: float, y: float) -> (int, int):
        return x // CHUNK_SIZE, y // CHUNK_SIZE

    def generate_seed(self):
        self.seed = random.randint(1, 1000)
