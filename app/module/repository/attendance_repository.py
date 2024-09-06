import json
import os
from datetime import datetime

from app.config.settings import DATA_PATH


class AttendanceRepository:
    """出勤簿のパスのリポジトリーを担う
    保存するファイル名の先頭にはかならず、年度を入れて保存する
    またこれを取り出す用のキーも先頭に年度を入れる
    """

    attendance_xlsx_path = os.path.join(DATA_PATH, "attendance_app.json")

    def save_attendance_path(self, *, key, attendance_path: str) -> None:
        attendance_data = {}

        if os.path.exists(self.attendance_xlsx_path):
            with open(self.attendance_xlsx_path, "r") as f:
                try:
                    attendance_data = json.load(f)
                except json.JSONDecodeError:
                    attendance_data = {}

        attendance_data[key] = attendance_path

        with open(self.attendance_xlsx_path, "w") as f:
            json.dump(attendance_data, f, indent=4)

    def get_attendance_path(self, *, key: str) -> str:
        if os.path.exists(self.attendance_xlsx_path):
            with open(self.attendance_xlsx_path, "r") as f:
                try:
                    attendance_data: dict[str, str] = json.load(f)
                    return attendance_data.get(key, "")
                except json.JSONDecodeError:
                    return ""

    def get_attendance_path_by_year(self, *, year) -> str:
        if os.path.exists(self.attendance_xlsx_path):
            with open(self.attendance_xlsx_path, "r") as f:
                try:
                    attendance_data: dict[str, str] = json.load(f)
                    for key, value in attendance_data.items():
                        if year in key:
                            return key, value
                except json.JSONDecodeError:
                    return ""

    def delete_attendance_path(self, *, key: str) -> None:
        if os.path.exists(self.attendance_xlsx_path):
            with open(self.attendance_xlsx_path, "r") as f:
                try:
                    attendance_data = json.load(f)
                    attendance_data.pop(key, None)
                    with open(self.attendance_xlsx_path, "w") as f:
                        json.dump(attendance_data, f, indent=4)
                except json.JSONDecodeError:
                    pass
