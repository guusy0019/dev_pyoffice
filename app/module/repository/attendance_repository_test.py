import unittest

from app.module.repository.attendance_repository import AttendanceRepository


class TestAttendanceRepository(unittest.TestCase):

    def setUp(self):
        self.attendance_repository = AttendanceRepository()
        self.attendance_path = "C:\\Users\\matty\\doc\\（sample）出勤簿.xlsx"
        self.attendance_path_key = "2024（sample）出勤簿.xlsx"

    def test_save_attendance_path(self):
        self.attendance_repository.save_attendance_path(
            key=self.attendance_path_key, attendance_path=self.attendance_path
        )
        data = self.attendance_repository.get_attendance_path(
            key=self.attendance_path_key
        )
        self.assertEqual(data, self.attendance_path)

    def test_get_attendance_path(self):
        self.attendance_repository.save_attendance_path(
            key=self.attendance_path_key, attendance_path=self.attendance_path
        )
        data = self.attendance_repository.get_attendance_path(
            key=self.attendance_path_key
        )
        self.assertEqual(data, self.attendance_path)

    def test_get_attendance_path_by_year(self):
        test_year = "2024"
        key, value = self.attendance_repository.get_attendance_path_by_year(
            year=test_year
        )
        return key, value

    def test_delete_attendance_path(self):
        self.attendance_repository.save_attendance_path(
            key=self.attendance_path_key, attendance_path=self.attendance_path
        )
        self.attendance_repository.delete_attendance_path(key=self.attendance_path_key)
        data = self.attendance_repository.get_attendance_path(
            key=self.attendance_path_key
        )
        self.assertEqual(data, "")
