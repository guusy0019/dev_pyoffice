import os
import customtkinter

from app.ui.widget.file_dialog_widget import FileDialogWidget

from app.module.application.usecase.attendance_usecase import AttendanceUsecase


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
            command_button_text="ファイルを選択",
            file_name="出勤シート",
            readable_file_types="*.xlsx",
            initial_dir=initial_dir,
        )
        self.file_dialog.grid(row=0, column=0, padx=10, pady=20, sticky="ew")

        # 出勤シートが保存されているか確認
        attendance_service = AttendanceUsecase()
        if attendance_service.get_initial_attendance_path():
            self.file_dialog.textbox.insert(
                0, attendance_service.get_initial_attendance_path()
            )

    def button_select_callback(self):
        file_path = self.file_dialog.textbox.get()

        attendance_service = AttendanceUsecase()

        if file_path:
            attendance_service.save_attendance_path(attendance_path=file_path)
            self.file_dialog.textbox.delete(first_index=0, last_index="end")

        else:
            raise ValueError("ファイルパスが指定されていません")
