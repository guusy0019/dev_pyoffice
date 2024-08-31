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

from app.ui.page.home_page import HomePage
from app.ui.page.launcher_page import LauncherPage
from app.ui.page.todo_page import ThirdPage


class AppLayout(BaseCtkLayout):
    def __init__(self, route_handler):
        super().__init__()
        self.route_handler = route_handler

        # Load images
        self.large_test_image = customtkinter.CTkImage(
            Image.open(os.path.join(IMAGE_PATH, "large_test_image.png")),
            size=(500, 150),
        )
        self.image_icon_image = customtkinter.CTkImage(
            Image.open(os.path.join(IMAGE_PATH, "image_icon_light.png")), size=(20, 20)
        )

        # Create instances of each page
        self.home_frame = HomePage(self, self.large_test_image, self.image_icon_image)
        self.second_frame = LauncherPage(self)
        self.third_frame = ThirdPage(self)

        # Create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

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

        self.frame_2_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="ランチャー",
            fg_color=FG_COLOR,
            text_color=TEXT_COLOR,
            hover_color=HOVER_COLOR,
            command=lambda: self.route_handler("frame_2"),
            image=self.launcher_icon,
            anchor="w",
        )
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="TODO",
            fg_color=FG_COLOR,
            text_color=TEXT_COLOR,
            hover_color=HOVER_COLOR,
            command=lambda: self.route_handler("frame_3"),
            image=None,
            anchor="w",
        )
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        # 外観モードのウィジェットの配置
        self.appearance_mode_menu = AppearanceModeWidget(self.navigation_frame)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # スケーリングのウィジェットの配置
        self.scaling_optionemenu = ScalingOptionWidget(self.navigation_frame)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

    def select_button(self, name):
        """Select the button by name and update the appearance."""
        self.home_button.configure(
            fg_color=FG_COLOR if name == "home" else "transparent"
        )
        self.frame_2_button.configure(
            fg_color=FG_COLOR if name == "frame_2" else "transparent"
        )
        self.frame_3_button.configure(
            fg_color=FG_COLOR if name == "frame_3" else "transparent"
        )
