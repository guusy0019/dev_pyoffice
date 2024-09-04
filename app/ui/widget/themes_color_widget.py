import customtkinter


class ThemesColorWidget(customtkinter.CTkOptionMenu):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            values=["blue", "green", "dark-blue"],
            command=self.change_themes_color_event,
            **kwargs,
        )

    def change_themes_color_event(self, themes_color):
        try:
            customtkinter.set_default_color_theme(themes_color)
            print(f"Themes color changed to {themes_color}")
        except Exception as e:
            print(f"Error: {e}")


# なぜうまくいかん？
# customtkinter.navigation_frameのインスタンスでは変更不可のため、最初にプルダウンからテーマを選ばせる
# その後、テーマの文字列を保存してインスタンスを再起動するのが必要ぽいね
# まあ、後回しかな、ただテーマだけは保存しておく
