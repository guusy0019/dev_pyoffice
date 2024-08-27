import os
import tkinter as tk
import customtkinter

from app.config.constants import fonts


class LauncherPage(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)

        self.setup_form()

    def setup_form(self):

        # テキストボックスを表示する
        self.textbox = customtkinter.CTkEntry(
            master=self,
            placeholder_text="Excelファイルを選択してください(CSV可)",
            width=120,
            font=fonts,
        )
        self.textbox.grid(row=0, column=0, padx=10, pady=20, sticky="ew")

        # ボタンを表示する
        self.button = customtkinter.CTkButton(
            master=self,
            text="ファイルを選択",
            command=self.button_select_callback,
            font=fonts,
        )
        self.button.grid(row=0, column=1, padx=10, pady=20)

    def button_function(self):
        # テキストボックスに入力されたテキストを表示する
        print(self.textbox.get())

    def button_select_callback(self):
        """
        選択ボタンが押されたときのコールバック。ファイル選択ダイアログを表示する
        """
        # エクスプローラーを表示してファイルを選択する
        file_name = LauncherPage.file_read()

        if file_name is not None:
            # ファイルパスをテキストボックスに記入
            self.textbox.delete(first_index=0, last_index="end")
            self.textbox.insert(0, file_name)

    def button_open_callback(self):
        """
        開くボタンが押されたときのコールバック。暫定機能として、ファイルの中身をprintする
        """
        file_name = self.textbox.get()
        if file_name is not None or len(file_name) != 0:
            with open(file_name) as f:
                data = f.read()
                print(data)

    @staticmethod
    def file_read():
        """
        ファイル選択ダイアログを表示する
        """
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = tk.filedialog.askopenfilename(
            filetypes=[("csvファイル", "*.csv;*.xlsx;*.xls")], initialdir=current_dir
        )

        if len(file_path) != 0:
            return file_path
        else:
            # ファイル選択がキャンセルされた場合
            return None
