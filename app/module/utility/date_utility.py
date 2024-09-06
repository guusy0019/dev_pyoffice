import jpholiday
import datetime
import pytz
from app.config.settings import TIMEZONE


class DateUtility:

    def __init__(self):
        """タイムゾーンを設定し、今日の日付を取得"""
        self.timezone = pytz.timezone(TIMEZONE)
        self.today = datetime.datetime.now(self.timezone).date()

    @staticmethod
    def format_date(date: datetime.date, format: str = "%Y-%m-%d") -> str:
        """
        datetime.dateを指定したフォーマットで文字列に変換する。
        :param date: 変換する日付 (datetime.date)
        :param format: 日付フォーマット (デフォルトは 'YYYY-MM-DD')
        :return: フォーマット済みの日付文字列
        """
        return date.strftime(format)

    def get_this_month(self, date: datetime.date = None) -> str:
        """
        今月の日付を取得。引数を指定しない場合は今日の日付から取得。
        :param date: 指定の日付 (省略可)
        :return: フォーマットされた日付文字列
        """
        if date is None:
            date = self.today
        return date.strftime("%Y-%m")

    def get_this_year(self, date: datetime.date = None) -> str:
        """
        今年の日付を取得。引数を指定しない場合は今日の日付から取得。
        :param date: 指定の日付 (省略可)
        :return: フォーマットされた日付文字列
        """
        if date is None:
            date = self.today
        return date.strftime("%Y")
