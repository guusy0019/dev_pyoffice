import os
import tkinter as tk
from PIL import Image, ImageTk
import customtkinter

from app.ui.widget.file_dialog_widget import FileDialogWidget
from app.module.utility.exec_shortcut_utility import ShortcutExecutor
from app.module.utility.get_shortcut_icon_utility import IconExtractor

from app.module.service.launcher_service import LauncherService


class LauncherPage(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        self.setup()

    def setup(self):

        # TODO initial_dirをlinuxにも対応させる
        kwargs = {
            "placeholder_text": "ランチャーに保存するショートカットを選択してください",
            "button_text": "ショートカットを選択",
            "custom_command": self.button_select_callback,
            "command_button_text": "ショートカットを保存",
            "file_name": "ショートカット",
            "readable_file_types": "*.lnk",
            "initial_dir": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs",
        }

        self.file_dialog = FileDialogWidget(master=self, **kwargs)
        self.file_dialog.grid(row=0, column=0, padx=10, pady=20, sticky="ew")

        self.launcher_list = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )

        launcher_service = LauncherService()
        all_launcher_dict: dict[str, str] = launcher_service.get_all_launch_path()

        icon_extractor = IconExtractor()
        shortcut_executor = ShortcutExecutor()
        for app_name, app_path in all_launcher_dict.items():
            icon = icon_extractor.get_icon(app_path)
            icon = ImageTk.PhotoImage(icon)
            self.launcher_list = customtkinter.CTkButton(
                master=self.launcher_list,
                text=app_name,
                image=icon,
                compound="left",
                command=lambda app_path=app_path: shortcut_executor.execute_shortcut(
                    shortcut_path=app_path
                ),
            )

        self.launcher_list.grid(row=1, column=0, padx=10, pady=20, sticky="ew")

    def button_select_callback(self):
        file_path = self.file_dialog.textbox.get()
        # file_pathで取得した最後の"/"以降の文字列を取得
        app_name = file_path.split("/")[-1].split(".")[0]

        launcher_service = LauncherService()

        if os.path.exists(file_path):
            launcher_service.save_launch_path(key=app_name, launch_app_path=file_path)
            # テキストボックスをクリア
            self.file_dialog.textbox.delete(0, tk.END)
        else:
            raise FileNotFoundError(f"{file_path} not found")

    def _delete_launcher(self, key: str):
        """指定したランチャーを削除して、残りのランチャーを返す"""
        launcher_service = LauncherService()
        launcher_service.delete_launch_path(key=key)
        return launcher_service.get_all_launch_path()

    def get_shortcut_icon(self, shortcut_path):
        """ショートカットのアイコンを取得"""
        icon_extractor = IconExtractor()
        return icon_extractor.get_icon(shortcut_path)
