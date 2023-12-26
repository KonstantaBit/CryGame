import pygame as pg
from .save_manager import SaveManager
from .scene_manager import SceneManager
from .settings_manager import SettingManager
from constants import WIDTH, HEIGHT


class App:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(App, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()

        self._running = True
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.scene_manager = SceneManager(self.screen)
        self.settings_manager = SettingManager()

    def terminate(self):
        self._running = False

    def run(self):
        while self._running:
            self.scene_manager.update()
            pg.display.flip()
            self.screen.fill((60, 60, 80))
