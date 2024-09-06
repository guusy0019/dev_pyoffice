import unittest

from app.module.usecase.attendance_usecase import AttendanceUsecase
from app.module.utility.date_utility import DateUtility


class TestAttendanceUseCase(unittest.TestCase):

    def setUp(self):
        self.test_year_date = "2024"
        self.attendance_usecase = AttendanceUsecase()
        self.attendance_path = "C:\\Users\\matty\\doc\\（sample）出勤簿.xlsx"
        self.attendance_path_key = "2024（sample）出勤簿.xlsx"

    def test_save_attendance_path(self):
        self.attendance_usecase.save_attendance_path(
            attendance_path=self.attendance_path
        )
        data = self.attendance_usecase.get_attendance_path(key=self.attendance_path_key)
        self.assertEqual(data, self.attendance_path)

    def test_get_attendance_path(self):
        data = self.attendance_usecase.get_attendance_path(key=self.attendance_path_key)
        self.assertEqual(data, self.attendance_path)

    def test_delete_attendance_path(self):
        self.attendance_usecase.delete_attendance_path(key=self.attendance_path_key)
        data = self.attendance_usecase.get_attendance_path(key=self.attendance_path_key)
        self.assertEqual(data, "")

    def test_get_initial_attendance_path(self):
        file_key = self.attendance_usecase.get_initial_attendance_path()
        self.assertEqual(file_key, self.test_year_date)

    def test_gen_key_name_by_attendance_path(self):
        date_utility = DateUtility()
        this_year = date_utility.get_this_year()
        file_name = self.attendance_path.split("\\")[-1]
        key = self.attendance_usecase._gen_key_name_by_attendance_path(
            attendance_path=self.attendance_path
        )
        self.assertEqual(key, f"{this_year}{file_name}")
