import pygame as pg
from pygame import Rect
import sys
from src.CryGame import SceneInterface, App
from src.GUI import Image, TextButton, ContainerRows
from paths import asset_path
import os
from constants import WIDTH, HEIGHT


class MainMenuScene(SceneInterface):
    def __init__(self):
        super().__init__()
        self.background = Image(Rect(0, 0, WIDTH, HEIGHT),
                                os.path.join(asset_path, 'image/menu/background.png'))

        x = (WIDTH - 500) / 2
        y = (HEIGHT - 400) / 2

        self.menu_container = ContainerRows(Rect(x, y, 500, 400), padding=2)
        self.title = TextButton(
            Rect(0, 0, 10, 10),
            255,
            255,
            "Гномы-геологи",
            55,
            pg.Color(200, 0, 200),
            os.path.join(asset_path, 'fonts/SourceSansPro-Regular.ttf')
        )
        self.menu_container.add(self.title)

        self.play_button = TextButton(
            Rect(0, 0, 10, 10),
            200,
            150,
            "Играть",
            35,
            pg.Color(255, 255, 255),
            os.path.join(asset_path, 'fonts/SourceSansPro-Light.ttf')
        )
        self.menu_container.add(self.play_button)

        # self.multiplayer_button = TextButton(
        #     Rect(0, 0, 10, 10),
        #     200,
        #     150,
        #     "Сетевая игра",
        #     35,
        #     pg.Color(255, 255, 255),
        #     os.path.join(asset_path, 'fonts/SourceSansPro-Light.ttf')
        # )
        # self.menu_container.add(self.multiplayer_button)

        # self.settings_button = TextButton(
        #     Rect(0, 0, 10, 10),
        #     200,
        #     150,
        #     "Настройки",
        #     35,
        #     pg.Color(255, 255, 255),
        #     os.path.join(asset_path, 'fonts/SourceSansPro-Light.ttf')
        # )
        # self.menu_container.add(self.settings_button)

        self.exit_button = TextButton(
            Rect(0, 0, 10, 10),
            200,
            150,
            "Выйти",
            35,
            pg.Color(255, 255, 255),
            os.path.join(asset_path, 'fonts/SourceSansPro-Light.ttf')
        )
        self.menu_container.add(self.exit_button)

        self.add_scene_object(self.background)
        self.add_scene_object(self.menu_container)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.exit_button.mouse_over():
                    pg.quit()
                    sys.exit()
                elif self.play_button.mouse_over():
                    App().scene_manager.current_scene += 1