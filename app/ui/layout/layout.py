import os
import customtkinter
from PIL import Image
from app.config.settings import (
    IMAGE_PATH,
    TEXT_COLOR,
    HOVER_COLOR,
    FG_COLOR,
    FONTS,
)
from app.ui.layout._base_ctk_layout import BaseCtkLayout
from app.ui.page.home_page import HomePage
from app.ui.page.launcher_page import LauncherPage
from app.ui.page.todo_page import TodoPage
from app.ui.page.attendance_page import AttendancePage
from app.ui.widget.appearance_mode_widget import AppearanceModeWidget
from app.ui.widget.scaling_option_widget import ScalingOptionWidget

class AppLayout(BaseCtkLayout):
    def __init__(self):
        super().__init__()

        self.large_test_image = customtkinter.CTkImage(
            Image.open(os.path.join(IMAGE_PATH, "large_test_image.png")),
            size=(500, 150),
        )
        self.image_icon_image = customtkinter.CTkImage(
            Image.open(os.path.join(IMAGE_PATH, "image_icon_light.png")),
            size=(20, 20)
        )

        self.home_frame = HomePage(self, self.large_test_image, self.image_icon_image)
        self.launcher_frame = LauncherPage(self)
        self.todo_frame = TodoPage(self)
        self.attendance_frame = AttendancePage(self)

        self.frames = {
            "home": self.home_frame,
            "launcher": self.launcher_frame,
            "todo": self.todo_frame,
            "attendance": self.attendance_frame,
        }

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.button_info_list = [
            {"name": "home", "text": "ホーム", "icon": self.home_icon},
            {"name": "launcher", "text": "ランチャー", "icon": self.launcher_icon},
            {"name": "todo", "text": "TODO", "icon": self.todo_icon},
            {"name": "attendance", "text": "出勤シート", "icon": self.attendance_icon},
        ]

        self.buttons = {}

        for i, info in enumerate(self.button_info_list, start=1):
            button = customtkinter.CTkButton(
                self.navigation_frame,
                corner_radius=0,
                height=40,
                border_spacing=10,
                text=info["text"],
                fg_color=FG_COLOR,
                text_color=TEXT_COLOR,
                hover_color=HOVER_COLOR,
                image=info["icon"],
                anchor="w",
                command=lambda name=info["name"]: self.select_frame_by_name(name),
            )
            button.grid(row=i, column=0, sticky="ew")
            self.buttons[info["name"]] = button

        # 外観モードのウィジェットの配置
        self.appearance_mode_menu = AppearanceModeWidget(self.navigation_frame)
        self.appearance_mode_menu.grid(row=7, column=0, padx=20, pady=(10, 20))

        # スケーリングのウィジェットの配置
        self.scaling_optionemenu = ScalingOptionWidget(self.navigation_frame)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # 初期フレームの設定
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        self.select_button(name)

        for frame_name, frame in self.frames.items():
            if frame_name == name:
                frame.grid(row=0, column=1, sticky="nsew")
            else:
                frame.grid_forget()

    def select_button(self, name):
        for button_name, button in self.buttons.items():
            button.configure(
                fg_color=FG_COLOR if button_name == name else "transparent"
            )