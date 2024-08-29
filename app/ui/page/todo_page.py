import customtkinter
import tkinter as tk


class ThirdPage(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)

        self.todo_entry = customtkinter.CTkEntry(
            self, placeholder_text="Enter a task..."
        )
        self.todo_entry.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        self.todo_listbox = tk.Listbox(self, height=15, font=("Arial", 12))
        self.todo_listbox.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        self.add_task_button = customtkinter.CTkButton(
            self, text="Add Task", command=self.add_task
        )
        self.add_task_button.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        self.remove_task_button = customtkinter.CTkButton(
            self, text="Remove Selected Task", command=self.remove_task
        )
        self.remove_task_button.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

    def add_task(self):
        task = self.todo_entry.get()
        if task:
            self.todo_listbox.insert("end", task)
            self.todo_entry.delete(0, "end")

    def remove_task(self):
        selected_task_index = self.todo_listbox.curselection()
        if selected_task_index:
            self.todo_listbox.delete(selected_task_index)
