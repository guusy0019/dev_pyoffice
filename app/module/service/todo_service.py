class ToDoService:
    def add_task(self, listbox, task):
        listbox.insert("end", task)

    def remove_task(self, listbox, index):
        listbox.delete(index)
