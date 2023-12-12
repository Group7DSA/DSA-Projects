import tkinter as tk
from tkinter import simpledialog, messagebox
import json

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append({'task': task, 'done': False})
        self.save_tasks()
        print(f'Task "{task}" added.')

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            deleted_task = self.tasks.pop(index)
            self.save_tasks()
            print(f'Task "{deleted_task["task"]}" deleted.')
        else:
            print('not deleted.')

    def mark_as_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['done'] = True
            self.save_tasks()
            print(f'Task "{self.tasks[index]["task"]}" marked as done.')
        else:
            print('is not done.')

    def retrieve_tasks(self):
        return self.tasks

    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file)

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            pass


class ToDoListGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.todo_list = ToDoList()

        self.menu_label = tk.Label(master, text="\nMenu:")
        self.menu_label.pack()

        self.menu_options = [
            "1. Add Task",
            "2. Delete Task",
            "3. Mark Task as Done",
            "4. Display To Do List",
            "5. Exit"
        ]

        self.choice_var = tk.StringVar(master)
        self.choice_var.set(self.menu_options[0])
        self.choice_menu = tk.OptionMenu(master, self.choice_var, *self.menu_options)
        self.choice_menu.pack()

        self.enter_button = tk.Button(master, text="Enter", command=self.handle_choice, bg='#3f301d', fg='#FFFFFF', bd=2)
        self.enter_button.pack()

        self.output_text = tk.Text(master, height=10, width=40, bg='#a8ba9a', fg='#996888')
        self.output_text.pack()

        self.display_tasks()

    def handle_choice(self):
        choice = self.choice_var.get().split('.')[0]

        if choice == '1':
            task = simpledialog.askstring("Add Task", "Enter the task:")
            if task:
                self.todo_list.add_task(task)
                self.display_message(f'Task "{task}" added.')
        elif choice == '2':
            index = simpledialog.askinteger("Delete Task", "Enter the task index to delete:")
            if index is not None:
                self.todo_list.delete_task(index - 1)
                self.display_message(f'Task at index {index} deleted.')
        elif choice == '3':
            index = simpledialog.askinteger("Mark Task as Done", "Enter the task index to mark as done:")
            if index is not None:
                self.todo_list.mark_as_done(index - 1)
                self.display_message(f'Task at index {index} marked as done.')
        elif choice == '4':
            self.display_tasks()
        elif choice == '5':
            self.display_message("Exiting the program")
            self.master.destroy()

    def display_tasks(self):
        tasks = self.todo_list.retrieve_tasks()
        self.output_text.delete(1.0, tk.END)
        if not tasks:
            self.output_text.insert(tk.END, 'The to-do list is empty.')
        else:
            self.output_text.insert(tk.END, 'To-Do List:\n')
            for i, task in enumerate(tasks):
                status = 'Done' if task['done'] else 'Not Done'
                self.output_text.insert(tk.END, f'{i + 1}. {task["task"]} - {status}\n')

    def display_message(self, message):
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, message)


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListGUI(root)
    root.mainloop()
