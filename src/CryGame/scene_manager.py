from src.CryGame.scene import SceneInterface


class SceneManager:
    def __init__(self, screen):
        self.scenes: list[SceneInterface] = list()
        self.current_scene = 0
        self.screen = screen

    def update(self) -> None:
        if not self.scenes:
            return
        self.scenes[self.current_scene].update()

    def add_scene(self, scene: SceneInterface) -> None:
        scene.set_screen(self.screen)
        self.scenes.append(scene)
