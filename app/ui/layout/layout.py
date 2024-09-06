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

from app.ui.widget.appearance_mode_widget import AppearanceModeWidget
from app.ui.widget.scaling_option_widget import ScalingOptionWidget
from app.ui.widget.themes_color_widget import ThemesColorWidget

from app.ui.page.home_page import HomePage
from app.ui.page.launcher_page import LauncherPage
from app.ui.page.todo_page import TodoPage
from app.ui.page.attendance_page import AttendancePage


class AppLayout(BaseCtkLayout):
    def __init__(self, route_handler):
        super().__init__()
        self.route_handler = route_handler

        # TODO 設定ページでテーマを変更できるようにする
        # customtkinter.set_default_color_theme("blue")

        # Load images
        self.large_test_image = customtkinter.CTkImage(
            Image.open(os.path.join(IMAGE_PATH, "large_test_image.png")),
            size=(500, 150),
        )
        self.image_icon_image = customtkinter.CTkImage(
            Image.open(os.path.join(IMAGE_PATH, "image_icon_light.png")), size=(20, 20)
        )

        self.home_frame = HomePage(self, self.large_test_image, self.image_icon_image)
        self.launcher_frame = LauncherPage(self)
        self.todo_frame = TodoPage(self)
        self.attendance_frame = AttendancePage(self)

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.home_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="ホーム",
            fg_color=FG_COLOR,
            text_color=TEXT_COLOR,
            hover_color=HOVER_COLOR,
            image=self.home_icon,
            anchor="w",
            command=lambda: self.route_handler("home"),
        )
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.launcher_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="ランチャー",
            fg_color=FG_COLOR,
            text_color=TEXT_COLOR,
            hover_color=HOVER_COLOR,
            command=lambda: self.route_handler("launcher"),
            image=self.launcher_icon,
            anchor="w",
        )
        self.launcher_button.grid(row=2, column=0, sticky="ew")

        self.todo_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="TODO",
            fg_color=FG_COLOR,
            text_color=TEXT_COLOR,
            hover_color=HOVER_COLOR,
            command=lambda: self.route_handler("todo"),
            image=self.todo_icon,
            anchor="w",
        )
        self.todo_button.grid(row=3, column=0, sticky="ew")

        self.attendance_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="出勤シート",
            fg_color=FG_COLOR,
            text_color=TEXT_COLOR,
            hover_color=HOVER_COLOR,
            command=lambda: self.route_handler("attendance"),
            image=self.attendance_icon,
            anchor="w",
        )
        self.attendance_button.grid(row=4, column=0, sticky="ew")

        # 外観モードのウィジェットの配置
        self.appearance_mode_menu = AppearanceModeWidget(self.navigation_frame)
        self.appearance_mode_menu.grid(row=7, column=0, padx=20, pady=(10, 20))

        # スケーリングのウィジェットの配置
        self.scaling_optionemenu = ScalingOptionWidget(self.navigation_frame)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # # テーマカラーのウィジェットの配置
        # self.themes_color_widget = ThemesColorWidget(self)
        # self.themes_color_widget.grid(row=9, column=0, padx=20, pady=(10, 20))

    def select_button(self, name):

        self.home_button.configure(
            fg_color=FG_COLOR if name == "home" else "transparent"
        )
        self.launcher_button.configure(
            fg_color=FG_COLOR if name == "launcher" else "transparent"
        )
        self.todo_button.configure(
            fg_color=FG_COLOR if name == "todo" else "transparent"
        )
        self.attendance_button.configure(
            fg_color=FG_COLOR if name == "attendance" else "transparent"
        )
