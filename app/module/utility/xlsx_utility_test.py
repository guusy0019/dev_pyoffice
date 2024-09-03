import unittest
from openpyxl import Workbook

from app.module.utility.xlsx_utility import XlsxUtility


class TestXlsxUtility(unittest.TestCase):

    def setUp(self):
        self.xlsx_utility = XlsxUtility()
        self.xlsx_path = "C:\\Users\\matty\\doc\\（sample）出勤簿.xlsx"
        self.xlsx_path_key = "（sample）出勤簿.xlsx"

    def test_load_workbook(self):
        workbook: Workbook = self.xlsx_utility.load_workbook(self.xlsx_path)
        self.assertIsNotNone(workbook)

    def test_read_sheet(self):
        workbook: Workbook = self.xlsx_utility.load_workbook(self.xlsx_path)
        sheet_name = "202406"
        sheet = self.xlsx_utility.read_sheet(self.xlsx_path, sheet_name)
        self.assertIsNotNone(sheet)
