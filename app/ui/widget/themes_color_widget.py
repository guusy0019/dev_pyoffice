import customtkinter


class ThemesColorWidget(customtkinter.CTkOptionMenu):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            values=["blue", "green", "dark-blue"],
            command=self.change_themes_color_event,
            **kwargs
        )

    def change_themes_color_event(self, themes_color):
        customtkinter.set_default_color_theme(themes_color)


# なぜうまくいかん？
