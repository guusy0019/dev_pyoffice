import logging
import os

class MyLogger:
    def __init__(self, name, log_file='app.log', log_level=logging.DEBUG):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)

        # コンソールハンドラを作成
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)

        # ファイルハンドラを作成
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)

        # フォーマットを作成してハンドラに設定
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # ハンドラをロガーに追加（重複追加を防ぐためにチェック）
        if not self.logger.hasHandlers():
            self.logger.addHandler(console_handler)
            self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger

    def add_custom_handler(self, handler):
        self.logger.addHandler(handler)

# Loggerを初期化する関数
def init_logger(name, log_file='app.log', log_level=logging.DEBUG):
    return MyLogger(name, log_file, log_level).get_logger()
