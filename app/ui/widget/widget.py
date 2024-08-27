import customtkinter

import app.config.constants as constants


class CustomButton(customtkinter.CTkButton):
    def __init__(self, master, text, command, image=None, anchor="center"):
        super().__init__(
            master=master,
            text=text,
            command=command,
            image=image,
            anchor=anchor,
            corner_radius=0,
            height=40,
            border_spacing=10,
            fg_color=constants.fg_color,
            text_color=constants.text_color,
            hover_color=constants.hover_color,
        )


class CustomEntry(customtkinter.CTkEntry):
    def __init__(self, master, placeholder_text=""):
        super().__init__(master=master, placeholder_text=placeholder_text)
