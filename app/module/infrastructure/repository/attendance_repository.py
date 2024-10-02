import json
from pathlib import Path

from app.config.settings import DATA_PATH
from app.module.application.interface.attendance_interface import AttendanceRepositoryInterface


class AttendanceRepository(AttendanceRepositoryInterface):
    """出勤簿のパスのリポジトリーを担う
    保存するファイル名の先頭にはかならず、年度を入れて保存する
    またこれを取り出す用のキーも先頭に年度を入れる
    """

    repository_json_path = Path(DATA_PATH) / "attendance_app.json"

    def save_attendance_path(self, *, key: str, attendance_path: str) -> None:
        attendance_data = {}
        file_path = Path(attendance_path)

        if file_path.exists():
            with open(self.repository_json_path, "r") as f:
                try:
                    attendance_data = json.load(f)
                except json.JSONDecodeError:
                    attendance_data = {}

        attendance_data[key] = attendance_path

        with open(self.repository_json_path, "w") as f:
            json.dump(attendance_data, f, indent=4)

    def get_attendance_path(self, *, key: str) -> str:
        if self.repository_json_path.exists():
            with open(self.repository_json_path, "r") as f:
                try:
                    attendance_data: dict[str, str] = json.load(f)
                    return attendance_data.get(key, "")
                except json.JSONDecodeError:
                    return ""

    def get_attendance_path_by_year(self, *, year) -> str:
        if self.repository_json_path.exists():
            with open(self.repository_json_path, "r") as f:
                try:
                    attendance_data: dict[str, str] = json.load(f)
                    for k in attendance_data.keys():
                        if k.startswith(year):
                            return attendance_data[k]
                except Exception:
                    # ファイルが読み込めない場合は空文字を返す
                    return ""

    def delete_attendance_path(self, *, key: str) -> None:
        file_path = Path(self.repository_json_path)
        if file_path.exists():
            with open(self.repository_json_path, "r") as f:
                try:
                    attendance_data = json.load(f)
                    attendance_data.pop(key, None)
                    with open(self.repository_json_path, "w") as f:
                        json.dump(attendance_data, f, indent=4)
                except json.JSONDecodeError:
                    pass
