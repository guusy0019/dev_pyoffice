"""ショートカットのパスからアプリを実行する
windowsのみ対応
"""

import os


class ShortcutExecutor:
    def __init__(self, *, shortcut_path: str):
        self.shortcut_path = shortcut_path

    def execute_shortcut(self):
        # ショートカットファイルを実行
        if os.path.exists(self.shortcut_path):
            os.startfile(self.shortcut_path)
        else:
            print(f"Shortcut not found: {self.shortcut_path}")
