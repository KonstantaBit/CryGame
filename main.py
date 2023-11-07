from src.CryGame.app import App
from src.MainMenu.main_menu_scene import MainMenuScene

if __name__ == '__main__':
    app = App()
    app.scene_manager.add_scene(MainMenuScene())
    app.run()
