import os
import customtkinter
from PIL import Image

from app.config.settings import IMAGE_PATH, ICON_PATH
from app.ui.layout.menu_layout import MenuLayout
from app.ui.widget.appearance_mode_widget import AppearanceModeWidget
from app.ui.widget.scaling_option_widget import ScalingOptionWidget


class BaseCtkLayout(customtkinter.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title("pyoffice")
        self.geometry("1200x800")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # iconの設定
        self.iconbitmap(os.path.join(ICON_PATH, "icon.ico"))

        # メニューバーを配置
        self.menu_layout = MenuLayout(self)
        self.menu_layout.grid(row=0, column=0, sticky="ew")

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        # 外観モードのウィジェットの配置
        self.appearance_mode_menu = AppearanceModeWidget(self.navigation_frame)
        self.appearance_mode_menu.grid(row=7, column=0, padx=20, pady=(10, 20))

        # スケーリングのウィジェットの配置
        self.scaling_optionemenu = ScalingOptionWidget(self.navigation_frame)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # 各ページのアイコン画像を取得
        self.home_icon = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(IMAGE_PATH, "home_dark.png")),
            dark_image=Image.open(os.path.join(IMAGE_PATH, "home_light.png")),
            size=(20, 20),
        )
        self.launcher_icon = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(IMAGE_PATH, "launch_light.png")),
            dark_image=Image.open(os.path.join(IMAGE_PATH, "launch_dark.png")),
            size=(20, 20),
        )

        self.todo_icon = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(IMAGE_PATH, "todo_light.png")),
            dark_image=Image.open(os.path.join(IMAGE_PATH, "todo_dark.png")),
            size=(20, 20),
        )

        self.attendance_icon = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(IMAGE_PATH, "attendance_light.png")),
            dark_image=Image.open(os.path.join(IMAGE_PATH, "attendance_dark.png")),
            size=(20, 20),
        )
