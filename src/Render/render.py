from pygame import Surface
from src.CryGame import SceneObjectInterface, SaveManager, Save, Pos
from constants import CHUNK_SIZE, WIDTH, HEIGHT, TEXTURE_SIZE
from src.GUI import Text
import pygame as pg
from src.Entity.base_entity import ProbeFlag
import os
from paths import asset_path


class Render(SceneObjectInterface):
    def __init__(self, position: Pos):
        self.position: Pos = position
        self.zoom: float = 1
        save_manager = SaveManager()
        self.save: Save = save_manager.current

    def draw(self, display: Surface) -> None:
        self.save.manage_chunks([Save.get_chunk_number_by_cords(self.position.x, self.position.y)])
        for pos, chunk in self.save.chunks.items():
            x = pos[0] * TEXTURE_SIZE * CHUNK_SIZE + WIDTH // 2 - self.position.x * TEXTURE_SIZE
            y = pos[1] * TEXTURE_SIZE * CHUNK_SIZE + HEIGHT // 2 - self.position.y * TEXTURE_SIZE
            display.blit(chunk.texture, (x, y))

        for entity in self.save.entities:
            x = TEXTURE_SIZE * entity.position.x + WIDTH // 2 - self.position.x * TEXTURE_SIZE
            y = TEXTURE_SIZE * entity.position.y + HEIGHT // 2 - self.position.y * TEXTURE_SIZE
            if isinstance(entity, ProbeFlag):
                text = Text(pg.Rect(x, y, 200, 100), entity.contain, 20, pg.Color(255, 255, 255), os.path.join(asset_path, 'fonts/SourceSansPro-Light.ttf'))
                text.draw(display)
            display.blit(entity.texture, (x, y + 20))

        for entity in self.save.players:
            x = TEXTURE_SIZE * entity.position.x + WIDTH // 2 - self.position.x * TEXTURE_SIZE
            y = TEXTURE_SIZE * entity.position.y + HEIGHT // 2 - self.position.y * TEXTURE_SIZE
            display.blit(entity.texture, (x, y))
        self.save.update()
        self.position = self.save.players[0].position
