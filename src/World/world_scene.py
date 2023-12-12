from src.CryGame import SceneInterface
from src.Render import Render
import pygame as pg
import sys


class WorldScene(SceneInterface):
    def __init__(self):
        super().__init__()
        render = Render((0, 0))
        self.add_scene_object(render)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
