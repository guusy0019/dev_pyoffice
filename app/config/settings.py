import os
import platform

# プロジェクトのルートディレクトリ
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# OSに基づいた画像パスの設定
if platform.system() == "Windows":
    IMAGE_PATH = os.path.join(BASE_DIR, "assets\\images")
else:
    IMAGE_PATH = os.path.join(BASE_DIR, "assets/images")
