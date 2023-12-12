import random

from src.CryGame import App, SaveManager, BlockManager
from src.MainMenu import MainMenuScene, SinglePlayerMenuScene, MultiPlayerMenuScene
from src.World import WorldScene

if __name__ == '__main__':
    app = App()
    bm = BlockManager()
    sm = SaveManager()
    sm.create("test")
    bm.load_textures()
    app.scene_manager.add_scene(WorldScene())
    # app.scene_manager.add_scene(MainMenuScene())
    # app.scene_manager.add_scene(SinglePlayerMenuScene())
    # app.scene_manager.add_scene(MultiPlayerMenuScene())
    app.run()
