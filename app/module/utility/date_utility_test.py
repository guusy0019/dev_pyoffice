import unittest
import datetime

from app.module.utility.date_utility import DateUtility


class TestDateUtility(unittest.TestCase):

    def setUp(self):
        self.date_utility = DateUtility()
        self.today = datetime.date.today()

    def test_get_today(self):
        today = self.date_utility.get_today()
        formated_date = today.strftime("%Y-%m-%d")
        self.assertEqual(today, self.today)

    def test_get_all_holidays(self):
        holidays = DateUtility.get_all_holiday_this_year()
        self.assertTrue(len(holidays) > 0)
