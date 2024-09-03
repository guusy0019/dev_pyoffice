from app.module.repository.attendance_repository import AttendanceRepository


class AttendanceUsecase:

    def save_attendance_path(self, *, attendance_path: str):
        attendance_repository = AttendanceRepository()
        key = self.gen_key_name_by_path(attendance_path)
        return attendance_repository.save_attendance_path(
            key=key, attendance_path=attendance_path
        )

    def get_attendance_path(self, *, key: str) -> str:
        attendance_repository = AttendanceRepository()
        return attendance_repository.get_attendance_path(key=key)

    def delete_attendance_path(self, *, key: str) -> None:
        attendance_repository = AttendanceRepository()
        attendance_repository.delete_attendance_path(key=key)

    def gen_key_name_by_path(self, attendance_path: str) -> str:
        """最後のパスからキー名を生成する"""
        return attendance_path.split("\\")[-1]
