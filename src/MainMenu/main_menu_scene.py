import pygame as pg
import sys
from src.CryGame.scene import SceneInterface
from src.GUI import Button, Image, Panel, Text
from paths import assetPath
import os


class MainMenuScene(SceneInterface):
    def __init__(self):
        super().__init__()
        self.x = (1080 - 720) // 2
        self.y = (720 - 480) // 2
        self.a = Button(os.path.join(assetPath, 'image/UI/pageforward-hover.png'),
                        os.path.join(assetPath, 'image/UI/pageforward.png'),
                        10,
                        10
                        )
        self.b = Panel((self.x, self.y, 720, 480), 200, (0, 0, 0))
        self.c = Image(os.path.join(assetPath, 'image/menu/background.png'), 0, 0)
        self.add_scene_object(self.c)
        self.add_scene_object(self.b)
        self.add_scene_object(self.a)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
