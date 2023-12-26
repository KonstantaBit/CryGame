import os
import pickle
from paths import saves_path
from .save import Save


class SaveManager:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def __init__(self):
        self.current: Save

    def load(self, name):
        with open(os.path.join(saves_path, f"{name}_ser"), "rb") as file:
            self.current = pickle.load(file)

    def save_current(self):
        with open(os.path.join(saves_path, f"{self.current.name}_ser"), "wb") as file:
            pickle.dump(self.current, file)

    def create(self, name):
        self.current = Save(name)
        self.current.generate_seed()
        self.save_current()
        print(1)
