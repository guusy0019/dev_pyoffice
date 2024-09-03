import jpholiday
import datetime


class DateUtility:

    def __init__(self):
        self.today = datetime.date.today()

    @staticmethod
    def format_date(date: datetime.date, format: str = "%Y-%m-%d") -> str:
        """日付を指定したフォーマットで文字列に変換する。"""
        return date.strftime(format)

    @staticmethod
    def is_holiday(date: datetime.date) -> bool:
        """今日の日付が祝日かどうかを判定する。"""
        return jpholiday.is_holiday(date)

    @staticmethod
    def is_weekday(date: datetime.date) -> bool:
        """今日の日付が平日かどうかを判定する。"""
        return not jpholiday.is_holiday(date) and date.weekday() < 5

    @staticmethod
    def get_today() -> datetime.date:
        """今日の日付を取得する。"""
        return datetime.date.today()

    @staticmethod
    def get_yesterday() -> datetime.date:
        """昨日の日付を取得する。"""
        return datetime.date.today() - datetime.timedelta(days=1)

    @staticmethod
    def get_tomorrow() -> datetime.date:
        """明日の日付を取得する。"""
        return datetime.date.today() + datetime.timedelta(days=1)

    @staticmethod
    def get_first_day_of_month() -> datetime.date:
        """今月の初日を取得する。"""
        return datetime.date.today().replace(day=1)

    @staticmethod
    def get_last_day_of_month() -> datetime.date:
        """今月の最終日を取得する。"""
        return datetime.date.today().replace(
            day=1, month=datetime.date.today().month + 1
        ) - datetime.timedelta(days=1)

    @staticmethod
    def get_first_day_of_next_month() -> datetime.date:
        """翌月の初日を取得する。"""
        return datetime.date.today().replace(
            day=1, month=datetime.date.today().month + 1
        )

    @staticmethod
    def get_last_day_of_previous_month() -> datetime.date:
        """先月の最終日を取得する。"""
        return datetime.date.today().replace(day=1) - datetime.timedelta(days=1)

    @staticmethod
    def get_all_holiday_this_year() -> list[datetime.date]:
        """今年の祝日を取得する。"""
        return jpholiday.year_holidays(datetime.date.today().year)
