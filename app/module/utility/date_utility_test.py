import unittest
import datetime

from app.module.utility.date_utility import DateUtility


class TestDateUtility(unittest.TestCase):

    def test_format_date(self):
        date_utility = DateUtility()
        now = datetime.datetime.now()
        data = date_utility.format_date(now, format="%Y-%m-%d-%H-%M-%S")
        return None

    def test_get_month_date(self):
        date_utility = DateUtility()
        data = date_utility.get_this_month()
        return None
