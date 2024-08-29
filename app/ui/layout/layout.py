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
from app.ui.page.todo_page import ThirdPage


class AppLayout(BaseCtkLayout):
    def __init__(self, route_handler):
        super().__init__()
        self.route_handler = route_handler

        # Load images
        image_path = IMAGE_PATH
        self.large_test_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "large_test_image.png")),
            size=(500, 150),
        )
        self.image_icon_image = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20)
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
            image=None,
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
            image=None,
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

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(
            self.navigation_frame,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event,
        )
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        self.scaling_optionemenu = customtkinter.CTkOptionMenu(
            self.navigation_frame,
            values=["80%", "90%", "100%", "110%", "120%"],
            command=self.change_scaling_event,
        )
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        self.scaling_optionemenu.set("100%")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def select_button(self, name):
        """Select the button by name and update the appearance."""
        self.home_button.configure(
            fg_color=("gray75", "gray25") if name == "home" else "transparent"
        )
        self.frame_2_button.configure(
            fg_color=("gray75", "gray25") if name == "frame_2" else "transparent"
        )
        self.frame_3_button.configure(
            fg_color=("gray75", "gray25") if name == "frame_3" else "transparent"
        )

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
