import openpyxl
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet


class XlsxUtility:

    @staticmethod
    def load_workbook(file_path: str) -> Workbook:
        """
        指定されたファイルパスからExcelワークブックを読み込む。

        :param file_path: 読み込むExcelファイルのパス
        :return: 読み込まれたWorkbookオブジェクト
        """
        return openpyxl.load_workbook(file_path)

    @staticmethod
    def save_workbook(workbook: Workbook, file_path: str) -> None:
        """
        指定されたファイルパスにExcelワークブックを保存する。

        :param workbook: 保存するWorkbookオブジェクト
        :param file_path: 保存先のファイルパス
        """
        workbook.save(file_path)

    @staticmethod
    def read_cell(file_path: str, sheet_name: str, cell: str) -> any:
        """
        指定されたシートの特定のセルからデータを読み込む。

        :param file_path: 読み込むExcelファイルのパス
        :param sheet_name: 対象のシート名
        :param cell: 読み込むセル（例: "A1"）
        :return: 読み込んだデータ
        """
        workbook = XlsxUtility.load_workbook(file_path)
        sheet = workbook[sheet_name]
        return sheet[cell].value

    @staticmethod
    def write_cell(file_path: str, sheet_name: str, cell: str, value: any) -> None:
        """
        指定されたシートの特定のセルにデータを書き込む。

        :param file_path: 読み込むExcelファイルのパス
        :param sheet_name: 対象のシート名
        :param cell: 書き込むセル（例: "A1"）
        :param value: 書き込むデータ
        """
        workbook = XlsxUtility.load_workbook(file_path)
        sheet = workbook[sheet_name]
        sheet[cell].value = value
        XlsxUtility.save_workbook(workbook, file_path)

    @staticmethod
    def read_sheet(file_path: str, sheet_name: str) -> list[list[any]]:
        """
        指定されたシート全体のデータを2次元リストで読み込む。

        :param file_path: 読み込むExcelファイルのパス
        :param sheet_name: 読み込むシート名
        :return: シート全体のデータを含む2次元リスト
        """
        workbook = XlsxUtility.load_workbook(file_path)
        sheet = workbook[sheet_name]
        return [[cell.value for cell in row] for row in sheet.iter_rows()]

    @staticmethod
    def write_sheet(file_path: str, sheet_name: str, data: list[list[any]]) -> None:
        """
        指定されたシートに2次元リスト形式のデータを書き込む。

        :param file_path: 読み込むExcelファイルのパス
        :param sheet_name: 書き込むシート名
        :param data: 書き込むデータを含む2次元リスト
        """
        workbook = XlsxUtility.load_workbook(file_path)
        if sheet_name in workbook.sheetnames:
            sheet = workbook[sheet_name]
        else:
            sheet = workbook.create_sheet(title=sheet_name)

        for i, row in enumerate(data, start=1):
            for j, value in enumerate(row, start=1):
                sheet.cell(row=i, column=j, value=value)

        XlsxUtility.save_workbook(workbook, file_path)

    @staticmethod
    def add_sheet(file_path: str, sheet_name: str) -> None:
        """
        Excelファイルに新しいシートを追加する。

        :param file_path: 読み込むExcelファイルのパス
        :param sheet_name: 追加するシート名
        """
        workbook = XlsxUtility.load_workbook(file_path)
        workbook.create_sheet(title=sheet_name)
        XlsxUtility.save_workbook(workbook, file_path)

    @staticmethod
    def delete_sheet(file_path: str, sheet_name: str) -> None:
        """
        Excelファイルからシートを削除する。

        :param file_path: 読み込むExcelファイルのパス
        :param sheet_name: 削除するシート名
        """
        workbook = XlsxUtility.load_workbook(file_path)
        if sheet_name in workbook.sheetnames:
            del workbook[sheet_name]
            XlsxUtility.save_workbook(workbook, file_path)
        else:
            raise ValueError(f"シート名 '{sheet_name}' は存在しません。")
