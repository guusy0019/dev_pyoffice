import customtkinter

""" 
かえってわかりにくくなってしまうので使わないかな
"""


class ScalingOptionMenuWidget(customtkinter.CTkOptionMenu):
    def __init__(self, parent, values, command, default_value="100%", **kwargs):
        super().__init__(parent, values=values, command=command, **kwargs)
        self.set(default_value)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
