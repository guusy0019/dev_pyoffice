import os
import platform

# プロジェクトのルートディレクトリ main.pyがあるディレクトリ
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

ICON_PATH = os.path.join(BASE_DIR, "app\\assets")
IMAGE_PATH = os.path.join(BASE_DIR, "app\\assets\\images")
DATA_PATH = os.path.join(BASE_DIR, "app\\assets\\data")
LOG_FILE_PATH = os.path.join(BASE_DIR, "app\\logs\\app.log")


# ("ライトモード", "ダークモード")
TEXT_COLOR = ("gray10", "gray90")

HOVER_COLOR = ("gray70", "gray30")

# ボタンの背景色
FG_COLOR = "transparent"

# ("フォント名", フォントサイズ)
FONTS = ("meiryo", 15)
