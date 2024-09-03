import json
import os

from app.config.settings import DATA_PATH


class AttendanceRepository:
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
