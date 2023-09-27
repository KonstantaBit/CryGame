from scene import Scene


class SceneManager:
    def __init__(self, event_manager):
        self.scenes = list()
        self.current_scene = 0
        self.event_manager = event_manager

    def draw(self) -> None:
        if not self.scenes:
            return None
        pass

    def run(self):
        pass

    def add_scene(self, scene: Scene) -> None:
        self.scenes.append(scene)
