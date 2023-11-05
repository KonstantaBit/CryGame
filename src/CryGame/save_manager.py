import os
import pickle

from save import Save


class SaveManager:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SaveManager, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        os.chdir('../..')
        os.environ['CG_ROOT_FOLDER'] = os.path.abspath(os.curdir)

        self.current_save = None
        self.saves: list[Save] = list()
        self.folder = os.path.join(os.environ['CG_ROOT_FOLDER'], 'saves')

    def create_save(self, name):
        try:
            os.mkdir(os.path.join(self.folder, name))
            if self.current_save is None:
                self.current_save = 0
            else:
                self.current_save += 1
            self.saves.append(Save(name))
        except FileExistsError:
            print('Сохранение с таким именем уже есть')

    def freeze_save(self):
        with open(os.path.join(self.folder, self.get_current_save().name), 'wb') as file:
            pickle.dump(self.saves[self.current_save], file)

    def delete_save(self):
        pass

    def load_save(self):
        pass

    def get_current_save(self):
        return self.saves[self.current_save]