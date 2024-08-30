import json


class LauncherRepository:
    save_path = "app/assets/data/launcher_app.json"

    def __init__(self, db):
        pass

    def save_file_path(self, *, file_path, key):
        with open(self.save_path, "w") as f:
            json.dump({key: file_path}, f)

    def save_file_paths(self, *, file_paths: dict):
        with open(self.save_path, "w") as f:
            json.dump(file_paths, f)
