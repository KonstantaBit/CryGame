from src.CryGame.scene import SceneInterface


class SceneManager:
    def __init__(self, screen):
        self.scenes = list()
        self.current_scene = 0
        self.screen = screen

    def run(self) -> None:
        if not self.scenes:
            return
        self.scenes[self.current_scene].run()

    def add_scene(self, scene: SceneInterface) -> None:
        scene.set_screen(self.screen)
        scene.set_scene_manager(self)
        self.scenes.append(scene)
