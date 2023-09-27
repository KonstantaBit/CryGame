from scene_manager import SceneManager
from event_manager import EventManager


class App:
    def __init__(self):
        self.running = True
        self.width = 720
        self.height = 480
        self.event_manager = EventManager()
        self.scene_manager = SceneManager(self.event_manager)

    def terminate(self):
        self.running = False

    def run(self):
        while self.running:
            self.event_manager.run()
            self.scene_manager.run()
