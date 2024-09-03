import unittest

from app.module.service.attendance_service import AttendanceService


class TestAttendanceService(unittest.TestCase):

    def setUp(self) -> None:
        self.attendance_service = AttendanceService()
        self.attendance_path = "C:\\Users\\matty\\doc\\（sample）出勤簿.xlsx"
        self.attendance_path_key = "（sample）出勤簿.xlsx"

    def test_save_attendance_path(self):
        self.attendance_service.save_attendance_path(
            attendance_path=self.attendance_path
        )
        data = self.attendance_service.get_attendance_path(key=self.attendance_path_key)
        self.assertEqual(data, self.attendance_path)

    def test_get_attendance_path(self):
        data = self.attendance_service.get_attendance_path(key=self.attendance_path_key)
        self.assertEqual(data, self.attendance_path)

    def test_delete_attendance_path(self):
        self.attendance_service.delete_attendance_path(key=self.attendance_path_key)
        data = self.attendance_service.get_attendance_path(key=self.attendance_path_key)
        self.assertEqual(data, "")
