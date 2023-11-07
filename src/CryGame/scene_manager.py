from src.CryGame.scene import SceneInterface


class SceneManager:
    def __new__(cls, screen):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SceneManager, cls).__new__(cls)
        return cls.instance

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
        self.scenes.append(scene)
