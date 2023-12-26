from pygame import Surface
from src.CryGame import SceneObjectInterface, SaveManager, Save, Pos
from constants import CHUNK_SIZE, WIDTH, HEIGHT, TEXTURE_SIZE


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
            display.blit(entity.texture, (x, y))
        self.save.update()
        self.position = self.save.entities[0].position
