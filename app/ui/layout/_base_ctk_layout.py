import os
import customtkinter
from PIL import Image

from app.config.settings import IMAGE_PATH, ICON_PATH
from app.ui.layout.menu_layout import MenuLayout


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
