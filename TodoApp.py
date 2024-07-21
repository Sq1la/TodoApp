import tkinter as tk
from tkinter import ttk
from datetime import datetime

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        return f"Задача: {self.title}\nОписание: {self.description}\nВыполнено: {'Да' if self.completed else 'Нет'}"

class PriorityTask(Task):
    def __init__(self, title, description, priority):
        super().__init__(title, description)
        self.priority = priority

    def __str__(self):
        return f"Задача с приоритетом: {self.title}\nОписание: {self.description}\nПриоритет: {self.priority}\nВыполнено: {'Да' if self.completed else 'Нет'}"

class DeadlineTask(Task):
    def __init__(self, title, description, deadline):
        super().__init__(title, description)
        self.deadline = datetime.strptime(deadline, "%d.%m.%Y")

    def __str__(self):
        return f"Задача с дедлайном: {self.title}\nОписание: {self.description}\nДедлайн: {self.deadline.strftime('%d.%m.%Y')}\nВыполнено: {'Да' if self.completed else 'Нет'}"

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.complete()

    def show_tasks(self):
        tasks_info = ""
        for task in self.tasks:
            tasks_info += str(task) + "\n" + "-" * 20 + "\n"
        return tasks_info

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Список дел")
        self.root.configure(bg="#f0f0f0")

        self.todo_list = TodoList()

        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 12), background="#f0f0f0")
        style.configure("TButton", font=("Helvetica", 12), padding=5)
        style.configure("TEntry", font=("Helvetica", 12))
        style.configure("TCombobox", font=("Helvetica", 12))

        self.task_frame = ttk.LabelFrame(root, text="Добавить задачу", padding=10)
        self.task_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.type_label = ttk.Label(self.task_frame, text="Тип задачи")
        self.type_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.type_combo = ttk.Combobox(self.task_frame, values=["Обычная задача", "Задача с приоритетом", "Задача с дедлайном"])
        self.type_combo.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.type_combo.current(0)

        self.title_label = ttk.Label(self.task_frame, text="Название")
        self.title_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.title_entry = ttk.Entry(self.task_frame)
        self.title_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.description_label = ttk.Label(self.task_frame, text="Описание")
        self.description_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.description_entry = ttk.Entry(self.task_frame)
        self.description_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        self.priority_label = ttk.Label(self.task_frame, text="Приоритет (только для задач с приоритетом)")
        self.priority_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.priority_entry = ttk.Entry(self.task_frame)
        self.priority_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        self.deadline_label = ttk.Label(self.task_frame, text="Дедлайн (дд.мм.гггг, только для задач с дедлайном)")
        self.deadline_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.deadline_entry = ttk.Entry(self.task_frame)
        self.deadline_entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

        self.add_button = ttk.Button(self.task_frame, text="Добавить задачу", command=self.add_task)
        self.add_button.grid(row=5, column=0, columnspan=2, pady=10, sticky="ew")

        self.tasks_frame = ttk.LabelFrame(root, text="Задачи", padding=10)
        self.tasks_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.tasks_text = tk.Text(self.tasks_frame, width=50, height=15, font=("Helvetica", 12), bg="#ffffff", fg="#000000", bd=1, relief="solid")
        self.tasks_text.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.refresh_button = ttk.Button(self.tasks_frame, text="Обновить задачи", command=self.refresh_tasks)
        self.refresh_button.grid(row=1, column=0, pady=5, sticky="ew")

        self.manage_frame = ttk.LabelFrame(root, text="Управление задачами", padding=10)
        self.manage_frame.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

        self.remove_label = ttk.Label(self.manage_frame, text="Название для удаления")
        self.remove_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.remove_entry = ttk.Entry(self.manage_frame)
        self.remove_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.remove_button = ttk.Button(self.manage_frame, text="Удалить задачу", command=self.remove_task)
        self.remove_button.grid(row=1, column=0, columnspan=2, pady=5, sticky="ew")

        self.complete_label = ttk.Label(self.manage_frame, text="Название для завершения")
        self.complete_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.complete_entry = ttk.Entry(self.manage_frame)
        self.complete_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self.complete_button = ttk.Button(self.manage_frame, text="Завершить задачу", command=self.complete_task)
        self.complete_button.grid(row=3, column=0, columnspan=2, pady=5, sticky="ew")

        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(1, weight=1)
        self.tasks_frame.grid_rowconfigure(0, weight=1)

    def add_task(self):
        task_type = self.type_combo.get()
        title = self.title_entry.get()
        description = self.description_entry.get()
        
        if task_type == "Обычная задача":
            task = Task(title, description)
        elif task_type == "Задача с приоритетом":
            priority = self.priority_entry.get()
            task = PriorityTask(title, description, priority)
        elif task_type == "Задача с дедлайном":
            deadline = self.deadline_entry.get()
            task = DeadlineTask(title, description, deadline)
        else:
            return
        
        self.todo_list.add_task(task)
        self.clear_entries()
        self.refresh_tasks()

    def remove_task(self):
        title = self.remove_entry.get()
        self.todo_list.remove_task(title)
        self.clear_entries()
        self.refresh_tasks()

    def complete_task(self):
        title = self.complete_entry.get()
        self.todo_list.complete_task(title)
        self.clear_entries()
        self.refresh_tasks()

    def refresh_tasks(self):
        tasks_info = self.todo_list.show_tasks()
        self.tasks_text.delete(1.0, tk.END)
        self.tasks_text.insert(tk.END, tasks_info)

    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)
        self.deadline_entry.delete(0, tk.END)
        self.remove_entry.delete(0, tk.END)
        self.complete_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()