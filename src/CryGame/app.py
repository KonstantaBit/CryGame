import pygame as pg

from .scene_manager import SceneManager
from .event_manager import EventManager


class App:
    def __init__(self):
        self.running = True
        self.width = 720
        self.height = 480
        self.screen = pg.display.set_mode((self.width, self.height))

        self.event_manager = EventManager()
        self.scene_manager = SceneManager(self.screen)

    def terminate(self):
        self.running = False

    def run(self):
        while self.running:
            self.event_manager.run()
            self.scene_manager.run()
            pg.display.flip()
