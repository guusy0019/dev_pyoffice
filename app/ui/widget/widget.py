import customtkinter


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
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
        )


class CustomEntry(customtkinter.CTkEntry):
    def __init__(self, master, placeholder_text=""):
        super().__init__(master=master, placeholder_text=placeholder_text)
