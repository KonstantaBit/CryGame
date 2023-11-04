from src.core.scene import Scene
from src.scene_objects.background import Background


class DefaultScene(Scene):
    def __init__(self):
        super().__init__()
        self.scene_objects = [Background()]
