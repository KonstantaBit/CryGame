from src.CryGame.app import App
from src.MainMenu import MainMenuScene, SinglePlayerMenuScene, MultiPlayerMenuScene

if __name__ == '__main__':
    app = App()
    app.scene_manager.add_scene(MainMenuScene())
    app.scene_manager.add_scene(SinglePlayerMenuScene())
    app.scene_manager.add_scene(MultiPlayerMenuScene())
    app.run()
