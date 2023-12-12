from pygame import Surface
import pygame as pg
from src.CryGame import SceneObjectInterface, SaveManager, Save


class Render(SceneObjectInterface):
    def __init__(self, position: [float, float]):
        self.position: [float, float] = position
        self.zoom: float = 1
        save_manager = SaveManager()
        self.save: Save = save_manager.current

    def draw(self, display: Surface) -> None:
        self.save.manage_chunks([(0, 0)])
        for el in self.save.chunks.items():
            print(el)
            for i in range(64):
                for j in range(64):
                    self.image_ref = pg.image.load(el[1].blocks[i][j].texture).convert_alpha()
                    display.blit(self.image_ref, (i * 32, j * 32))