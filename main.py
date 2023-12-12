import random

from src.CryGame import App, SaveManager
from src.MainMenu import MainMenuScene, SinglePlayerMenuScene, MultiPlayerMenuScene
from src.World import WorldScene

if __name__ == '__main__':
    app = App()
    sm = SaveManager()
    sm.create("test")
    app.scene_manager.add_scene(WorldScene())
    # app.scene_manager.add_scene(MainMenuScene())
    # app.scene_manager.add_scene(SinglePlayerMenuScene())
    # app.scene_manager.add_scene(MultiPlayerMenuScene())
    app.run()
