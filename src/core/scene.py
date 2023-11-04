from pygame.surface import Surface

from src.core.scene_object import SceneObject


class Scene:
    def __init__(self):
        self.scene_objects = list()

    def draw(self, screen: Surface) -> None:
        for obj in self.scene_objects:
            obj.draw(screen)

    def add_scene_object(self, scene_object: SceneObject) -> None:
        self.scene_objects.append(scene_object)