import os
import tkinter as tk
import customtkinter

from app.ui.widget.file_dialog_widget import FileDialogWidget


class LauncherPage(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        self.setup()

    def setup(self):

        kwargs = {
            "placeholder_text": "ランチャーに保存する.exeファイルを選択してください",
            "button_text": "ファイルを選択",
            "custom_command": self.button_select_callback,
            "command_button_text": "パスを保存",
            "file_name": "実行ファイル",
            "readable_file_types": "*.exe",
        }

        self.file_dialog = FileDialogWidget(master=self, **kwargs)
        self.file_dialog.grid(row=0, column=0, padx=10, pady=20, sticky="ew")

    def button_select_callback(self):
        file_path = self.file_dialog.textbox.get()
        if os.path.exists(file_path):
            print("File exists")
        else:
            print("File does not exist")
