import pygame as pg

from .scene_manager import SceneManager


class App:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(App, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self._running = True
        self._width = 1080
        self._height = 720
        self.screen = pg.display.set_mode((self._width, self._height))
        self.scene_manager = SceneManager(self.screen)

    def terminate(self):
        self._running = False

    def run(self):
        while self._running:
            self.scene_manager.run()
            pg.display.flip()
