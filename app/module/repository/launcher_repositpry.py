import json
import os

from app.config.settings import BASE_DIR


class LauncherRepository:
    save_path = os.path.join(BASE_DIR, "app/assets/data/launcher_app.json")

    def save_launch_path(self, *, key: str, launch_app_path: str):
        launch_data = {}

        # 拡張子が.exeかどうかを確認
        if not launch_app_path.endswith(".exe"):
            raise ValueError("save_path's Extension must be .exe")

        if os.path.exists(self.save_path):
            with open(self.save_path, "r") as f:
                try:
                    # 既存のデータを読み込む
                    launch_data = json.load(f)
                except json.JSONDecodeError:
                    # ファイルが壊れているか、空の場合は無視する
                    launch_data = {}

        # 新しいキーと値を追加
        launch_data[key] = launch_app_path

        # ファイルに書き戻す
        with open(self.save_path, "w") as f:
            json.dump(launch_data, f, indent=4)

    def get_launch_path(self, *, key: str) -> str:

        if os.path.exists(self.save_path):
            with open(self.save_path, "r") as f:
                try:
                    launch_data: dict[str, str] = json.load(f)
                    # print("launch_data_type", type(launch_data))
                    return launch_data.get(key, "")
                except json.JSONDecodeError:
                    return ""

    def get_all_launch_path(self) -> dict[str, str]:
        if os.path.exists(self.save_path):
            with open(self.save_path, "r") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return {}
        return {}

    def delete_launch_path(self, *, key: str) -> None:
        if os.path.exists(self.save_path):
            with open(self.save_path, "r") as f:
                try:
                    launch_data = json.load(f)
                    launch_data.pop(key, None)
                    with open(self.save_path, "w") as f:
                        json.dump(launch_data, f, indent=4)
                except json.JSONDecodeError:
                    pass
