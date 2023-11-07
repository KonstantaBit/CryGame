import sys
import pygame as pg
from .scene_object import SceneObjectInterface


class SceneInterface:
    def __init__(self):
        self.screen = None
        self.scene_objects = list()

    def set_screen(self, screen: pg.Surface):
        self.screen = screen

    def draw(self) -> None:
        for obj in self.scene_objects:
            obj.draw(self.screen)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def run(self):
        self.handle_events()
        self.draw()

    def add_scene_object(self, scene_object: SceneObjectInterface) -> None:
        self.scene_objects.append(scene_object)
