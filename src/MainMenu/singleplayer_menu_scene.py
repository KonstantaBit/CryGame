import pygame as pg
from pygame import Rect
import sys
from src.CryGame import SceneInterface, SceneManager
from src.GUI import Image, TextButton, ContainerRows
from paths import asset_path
import os


class SinglePlayerMenuScene(SceneInterface):
    def __init__(self):
        super().__init__()
        self.background = Image(Rect(0, 0, 1080, 720),
                                os.path.join(asset_path, 'image/menu/background.png'))

        x = (1080 - 500) / 2
        y = (720 - 400) / 2

        self.menu_container = ContainerRows(Rect(x, y, 500, 400), padding=2)

        self.create_world_button = TextButton(
            Rect(0, 0, 10, 10),
            200,
            150,
            "Создать мир",
            35,
            pg.Color(255, 255, 255),
            os.path.join(asset_path, 'fonts/SourceSansPro-Light.ttf')
        )
        self.menu_container.add(self.create_world_button)

        self.delete_world_button = TextButton(
            Rect(0, 0, 10, 10),
            200,
            150,
            "Удалить мир",
            35,
            pg.Color(255, 255, 255),
            os.path.join(asset_path, 'fonts/SourceSansPro-Light.ttf')
        )
        self.menu_container.add(self.delete_world_button)

        self.back_button = TextButton(
            Rect(0, 0, 10, 10),
            200,
            150,
            "Назад",
            35,
            pg.Color(255, 255, 255),
            os.path.join(asset_path, 'fonts/SourceSansPro-Light.ttf')
        )
        self.menu_container.add(self.back_button)

        self.add_scene_object(self.background)
        self.add_scene_object(self.menu_container)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.back_button.mouse_over():
                    self.scene_manager.current_scene = 0