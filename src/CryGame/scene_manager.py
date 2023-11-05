from .scene import Scene
from .event_manager import EventManager


class SceneManager:
    def __new__(cls, screen):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SceneManager, cls).__new__(cls)
        return cls.instance

    def __init__(self, screen):
        self.scenes = list()
        self.current_scene = 0
        self.event_manager = EventManager()
        self.screen = screen

    def draw(self) -> None:
        if not self.scenes:
            return
        self.scenes[self.current_scene].draw(self.screen)

    def run(self) -> None:
        self.draw()

    def add_scene(self, scene: Scene) -> None:
        self.scenes.append(scene)
