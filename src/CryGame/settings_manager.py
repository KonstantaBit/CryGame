import json
import os
from paths import main_path


class SettingManager:
    def __init__(self):
        self._file = os.path.join(main_path, 'settings.json')
        if not os.path.exists(self._file):
            self._initial_settings()
        self._data: dict
        self._get_settings_from_file()

    def _initial_settings(self):
        self._data = {'width': 720, 'height': 480}
        self.save_settings_to_file()

    def _get_settings_from_file(self) -> None:
        with open(self._file, 'r') as file:
            self._data = json.load(file)

    def save_settings_to_file(self) -> None:
        with open(self._file, 'w') as file:
            json.dump(self._data, file)

    @property
    def data(self) -> dict:
        return self._data
