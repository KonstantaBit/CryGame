from src.core.app import App
from src.scenes.default_scene import DefaultScene

if __name__ == '__main__':
    app = App()
    app.scene_manager.add_scene(DefaultScene())
    app.run()
