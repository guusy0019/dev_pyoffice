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

        if name == "launcher":
            self.app_layout.launcher_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.app_layout.launcher_frame.grid_forget()

        if name == "todo":
            self.app_layout.todo_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.app_layout.todo_frame.grid_forget()

        if name == "attendance":
            self.app_layout.attendance_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.app_layout.attendance_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("launcher")

    def frame_3_button_event(self):
        self.select_frame_by_name("todo")

    def attendance_button_event(self):
        self.select_frame_by_name("attendance")
