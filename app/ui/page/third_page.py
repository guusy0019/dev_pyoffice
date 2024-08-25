import customtkinter
import tkinter as tk
from app.ui.widget.widget import CustomButton, CustomEntry


class ThirdPage(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)

        # Create Entry for ToDo input
        self.todo_entry = CustomEntry(self, placeholder_text="Add a new task")
        self.todo_entry.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        # Create Listbox for displaying ToDo tasks (using standard Tkinter Listbox)
        self.todo_listbox = tk.Listbox(self, height=15, font=("Arial", 12))
        self.todo_listbox.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        # Create Add Button
        self.add_task_button = CustomButton(
            self, text="Add Task", command=self.add_task
        )
        self.add_task_button.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        # Create Remove Button
        self.remove_task_button = CustomButton(
            self, text="Remove Selected Task", command=self.remove_task
        )
        self.remove_task_button.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

    def add_task(self):
        """Add a new task to the ToDo list."""
        task = self.todo_entry.get()
        if task:
            self.todo_listbox.insert("end", task)  # Listboxにタスクを追加
            self.todo_entry.delete(0, "end")  # Entryの内容をクリア

    def remove_task(self):
        """Remove the selected task from the ToDo list."""
        selected_task_index = (
            self.todo_listbox.curselection()
        )  # 選択されたタスクのインデックスを取得
        if selected_task_index:
            self.todo_listbox.delete(selected_task_index)  # Listboxからタスクを削除
