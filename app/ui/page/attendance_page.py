import os
import customtkinter

from app.ui.widget.file_dialog_widget import FileDialogWidget


class AttendancePage(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        self.setup()

    def setup(self):

        initial_dir = "C:\\Users"
        self.file_dialog = FileDialogWidget(
            master=self,
            placeholder_text="出勤シートを選択してください",
            button_text="シートを選択",
            custom_command=self.button_select_callback,
            command_button_text="ファイルを開く",
            file_name="出勤シート",
            readable_file_types="*.xlsx",
            initial_dir=initial_dir,
        )
        self.file_dialog.grid(row=0, column=0, padx=10, pady=20, sticky="ew")

    def button_select_callback(self):
        pass
