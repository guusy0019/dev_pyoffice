import tkinter as tk


class MenuLayout(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)

        self.setup_menu()

    def setup_menu(self):
        self.menu = tk.Menu(self)
        self.master.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)

        self.edit_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)

        self.config = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="設定", menu=self.config)

        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="終了", command=self.exit)

        self.edit_menu.add_command(label="Cut", command=self.cut)
        self.edit_menu.add_command(label="Copy", command=self.copy)
        self.edit_menu.add_command(label="Paste", command=self.paste)

        self.config.add_command(label="設定", command=self.to_settings)

    def new_file(self):
        pass

    def open_file(self):
        pass

    def save_file(self):
        pass

    def save_as_file(self):
        pass

    def exit(self):
        self.master.quit()

    def cut(self):
        pass

    def copy(self):
        pass

    def paste(self):
        pass

    def to_settings(self):
        pass
