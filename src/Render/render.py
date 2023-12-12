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
        size = int(32 * self.zoom)
        for el in self.save.chunks.items():
            print(el)
            for i in range(64):
                for j in range(64):
                    image = pg.transform.scale(el[1].blocks[i][j].texture, (size, size))
                    x = (size * i) + (64 * size * el[0][0])
                    y = (size * j) + (64 * size * el[0][1])
                    display.blit(image, (x, y))