import customtkinter
import os
import app.config.settings as settings
from PIL import Image
from app.ui.page.home_page import HomePage
from app.ui.page.launcher_page import LauncherPage
from app.ui.page.todo_page import ThirdPage
from app.ui.widget.widget import CustomButton


class AppLayout(customtkinter.CTk):
    def __init__(self, route_handler):
        super().__init__()

        self.route_handler = route_handler
        self.title("pyfile App!!")
        self.geometry("900x600")

        # Set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Load images
        image_path = settings.IMAGE_PATH
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

        self.home_button = CustomButton(
            self.navigation_frame,
            text="ホームページ!!",
            command=lambda: self.route_handler("home"),
            image=None,
            anchor="w",
        )
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = CustomButton(
            self.navigation_frame,
            text="ランチャーAPP!!",
            command=lambda: self.route_handler("frame_2"),
            image=None,
            anchor="w",
        )
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = CustomButton(
            self.navigation_frame,
            text="TODO APP!!",
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
