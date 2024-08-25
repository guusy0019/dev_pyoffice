class AppRoutes:
    def __init__(self, app_layout):
        self.app_layout = app_layout

    def select_frame_by_name(self, name):
        # Set button color for selected button
        self.app_layout.select_button(name)

        # Show selected frame
        if name == "home":
            self.app_layout.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.app_layout.home_frame.grid_forget()

        if name == "frame_2":
            self.app_layout.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.app_layout.second_frame.grid_forget()

        if name == "frame_3":
            self.app_layout.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.app_layout.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")
