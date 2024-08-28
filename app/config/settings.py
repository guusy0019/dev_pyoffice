import os
import platform

# プロジェクトのルートディレクトリ main.pyがあるディレクトリ
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# OSに基づいた画像パスの設定（いる？）
if platform.system() == "Windows":
    IMAGE_PATH = os.path.join(BASE_DIR, "app\\assets\\images")
else:
    IMAGE_PATH = os.path.join(BASE_DIR, "app/assets/images")

# ログファイルの設定
LOG_FILE_PATH = os.path.join(BASE_DIR, "app\\logs\\app.log")
