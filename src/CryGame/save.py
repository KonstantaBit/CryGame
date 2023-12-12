import os
import pickle
import random

from .chunck import Chunk
from paths import saves_path


class Save:
    def __init__(self, name):
        self.name = name
        self.seed = None
        self.chunks = dict()

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

    def save_chunk(self, x: int, y: int):
        with open(os.path.join(saves_path, self.name, "chunks", f"x{x}y{y}.dat"), "wb") as file:
            pickle.dump(self.chunks[(x, y)], file)
        del self.chunks[(x, y)]

    def save_all_chunks(self):
        for el in self.chunks.keys():
            self.save_chunk(*el)

    def manage_chunks(self, load_points: list[[int, int]]):
        for el in load_points:
            for i in range(1):
                for j in range(1):
                    self.load_chunk(el[0] - i, el[1] - j)

    @staticmethod
    def get_chunk_number_by_cords(x: float, y: float) -> (int, int):
        #  Сделать размер чанка костантным (где-то записать, чтобы был глобальный доступ)
        return x // 64, y // 64

    def generate_seed(self):
        self.seed = random.randint(1, 1000)
