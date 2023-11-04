from src.core.scene import Scene
from src.core.event_manager import EventManager


class SceneManager:
    def __init__(self, event_manager: EventManager, screen):
        self.scenes = list()
        self.current_scene = 0
        self.event_manager = event_manager
        self.screen = screen

    def draw(self) -> None:
        if not self.scenes:
            return
        self.scenes[self.current_scene].draw(self.screen)

    def run(self) -> None:
        self.draw()

    def add_scene(self, scene: Scene) -> None:
        self.scenes.append(scene)
