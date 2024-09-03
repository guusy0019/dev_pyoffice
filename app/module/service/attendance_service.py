from app.module.usecase.attendance_usecase import AttendanceUsecase


class AttendanceService:

    def save_attendance_path(self, *, attendance_path: str):
        attendance_usecase = AttendanceUsecase()
        return attendance_usecase.save_attendance_path(attendance_path=attendance_path)

    def get_attendance_path(self, *, key: str) -> str:
        attendance_usecase = AttendanceUsecase()
        return attendance_usecase.get_attendance_path(key=key)

    def delete_attendance_path(self, *, key: str) -> None:
        attendance_usecase = AttendanceUsecase()
        attendance_usecase.delete_attendance_path(key=key)
