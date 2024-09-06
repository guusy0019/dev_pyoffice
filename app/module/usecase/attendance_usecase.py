from datetime import datetime

from app.module.repository.attendance_repository import AttendanceRepository


class AttendanceUsecase:

    def save_attendance_path(self, *, attendance_path: str):
        """keyを一定にしたいかつ年度ごとのdateを入れたいので、パスからキーを生成して保存する
        example: C:\\Users\\matty\\doc\\（sample）出勤簿.xlsx -> 2024（sample）出勤簿.xlsx
        key -> 2024（sample）出勤簿.xlsx
        path -> C:\\Users\\matty\\doc\\2024（sample）出勤簿.xlsx

        """
        add_date_path = self._add_date_this_year(attendance_path)
        add_date_key = self._gen_key_name_by_attendance_path(attendance_path)
        attendance_repository = AttendanceRepository()
        attendance_repository.save_attendance_path(
            key=add_date_key, attendance_path=add_date_path
        )

    def get_attendance_path(self, *, key: str) -> str:
        attendance_repository = AttendanceRepository()
        is_valid = self._validate_input_str_including_year(key)
        if is_valid:
            return attendance_repository.get_attendance_path(key=key)
        else:
            raise ValueError("key is not including year")

    def get_initial_attendance_path(self) -> str:
        """初期読み込み時に今年の出勤簿のパスを取得する
        これをuiのコンストラクタで読み込んでもしNoneなら、textで
        「今年度の出勤.xlsxが見つからないので登録してくださいみたいな感じで表示やね
        """
        this_year = datetime.now().strftime("%Y")
        attendance_repository = AttendanceRepository()
        attendance_path = attendance_repository.get_attendance_path_by_year(
            year=this_year
        )
        if attendance_path:
            return attendance_path
        else:
            last_year = str(int(this_year) - 1)
            last_year_attendance: str = self._find_last_year_attendance_path(last_year)

    def _find_last_year_attendance_path(self, last_year) -> str:
        """昨年登録している場合は、そのパスを基準にファイルを作っちゃおう！"""
        attendance_repository = AttendanceRepository()
        attendance_path = attendance_repository.get_attendance_path_by_year(
            year=last_year
        )
        if attendance_path:
            pass
        else:
            return ""

    def delete_attendance_path(self, *, key: str) -> None:
        attendance_repository = AttendanceRepository()
        attendance_repository.delete_attendance_path(key=key)

    def _add_date_this_year(self, path: str) -> str:
        """パスの先頭に年度を追加する
        例）（sample）出勤簿.xlsx -> 2024（sample）出勤簿.xlsx
        """
        this_year = datetime.now().strftime("%Y")
        return f"{this_year}{path}"

    def _gen_key_name_by_attendance_path(self, attendance_path: str) -> str:
        """最後のパスから先頭に今年度をプラスしてキー名を生成する
        例）（sample）出勤簿.xlsx -> 2024（sample）出勤簿.xlsx
        """
        plane_file_name: str = attendance_path.split("\\")[-1]

        # ファイル名の先頭に%Y形式で年月を追加
        this_year = datetime.now().strftime("%Y")
        return f"{this_year}{plane_file_name}"

    def _validate_input_str_including_year(self, input_str: str) -> bool:
        """文字列の先頭が20から始まるかどうかを判定する
        2100年以降は知りません
        まあ、そのころには、pythonも終了でしょということで。
        """
        return input_str.startswith("20")
