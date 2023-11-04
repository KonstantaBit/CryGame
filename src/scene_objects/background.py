from pygame.surface import Surface

from src.core.scene_object import SceneObject


class Background(SceneObject):
    def __init__(self):
        super().__init__()
        self.color = (50, 50, 80)

    def draw(self, screen: Surface):
        screen.fill(self.color)