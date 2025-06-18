print("cassandra is pretty, but she's a rapist")
paul = "hello everyone"
print(paul)
num_one = 765
num_two = 677664


total = num_one + num_two
print(total)
user_name = input("what is your name: ")
print("welcome to UCU!!!",user_name)

Paul = "Handsome"
Yolo = "Cute"

Salim = "Funny"

print(Paul)

"""
Task Manager Script

Description:
-------------
This Python script is a simple command-line task manager that allows users to:
1. Add new tasks
2. View all tasks
3. Mark tasks as completed
4. Delete completed tasks

Tasks are stored in a JSON file called 'tasks.json' so that the task list is saved even after the script exits.
The script uses functions for modularity and error handling for robustness.

Author: ChatGPT
Date: May 2025
"""

import json
import os

TASKS_FILE = 'tasks.json'


def load_tasks():
    """Load tasks from the JSON file or return an empty list if file doesn't exist."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    """Save the list of tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks, description):
    """Add a new task to the list."""
    task = {'description': description, 'completed': False}
    tasks.append(task)
    print(f"Task added: {description}")


def view_tasks(tasks):
    """Display all tasks with their status."""
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = 'Done' if task['completed'] else 'Pending'
        print(f"{idx}. {task['description']} [{status}]")


def mark_task_completed(tasks, index):
    """Mark a task as completed."""
    try:
        tasks[index]['completed'] = True
        print(f"Task marked as completed: {tasks[index]['description']}")
    except IndexError:
        print("Invalid task number.")


def delete_completed_tasks(tasks):
    """Remove all completed tasks from the list."""
    before_count = len(tasks)
    tasks[:] = [task for task in tasks if not task['completed']]
    removed = before_count - len(tasks)
    print(f"{removed} completed task(s) removed.")


def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Completed Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            desc = input("Enter task description: ")
            add_task(tasks, desc)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            view_tasks(tasks)
            try:
                idx = int(input("Enter task number to mark as completed: ")) - 1
                mark_task_completed(tasks, idx)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            delete_completed_tasks(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()


"""
OOP Task Manager Script

Description:
-------------
This Python script implements a simple task manager using Object-Oriented Programming (OOP).
It allows users to:
1. Add new tasks
2. View all tasks
3. Mark tasks as completed
4. Delete completed tasks

The script uses two main classes:
- Task: represents a single task
- TaskManager: manages the list of tasks, handles file operations, and provides menu options

Tasks are saved to and loaded from a JSON file ('tasks.json') to persist data across runs.

Author: ChatGPT
Date: May 2025
"""

import json
import os

TASKS_FILE = 'tasks.json'


class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {'description': self.description, 'completed': self.completed}

    @staticmethod
    def from_dict(data):
        return Task(data['description'], data['completed'])


class TaskManager:
    def __init__(self, file_path=TASKS_FILE):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return [Task.from_dict(item) for item in data]
        return []

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, description):
        self.tasks.append(Task(description))
        print(f"Task added: {description}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for idx, task in enumerate(self.tasks, 1):
            status = 'Done' if task.completed else 'Pending'
            print(f"{idx}. {task.description} [{status}]")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print(f"Task marked as completed: {self.tasks[index].description}")
        else:
            print("Invalid task number.")

    def delete_completed_tasks(self):
        before_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task.completed]
        removed = before_count - len(self.tasks)
        print(f"{removed} completed task(s) removed.")

    def run(self):
        while True:
            print("\nTask Manager Menu:")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Delete Completed Tasks")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                desc = input("Enter task description: ")
                self.add_task(desc)
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.view_tasks()
                try:
                    idx = int(input("Enter task number to mark as completed: ")) - 1
                    self.mark_task_completed(idx)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == '4':
                self.delete_completed_tasks()
            elif choice == '5':
                self.save_tasks()
                print("Tasks saved. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    manager = TaskManager()
    manager.run()




print("cassandra is pretty, but she's a rapist")
paul = "hello everyone"
print(paul)
num_one = 765
num_two = 677664


total = num_one + num_two
print(total)
user_name = input("what is your name: ")
print("welcome to UCU!!!",user_name)

Paul = "Handsome"
Yolo = "Cute"

Salim = "Funny"

print(Paul)

"""
Task Manager Script

Description:
-------------
This Python script is a simple command-line task manager that allows users to:
1. Add new tasks
2. View all tasks
3. Mark tasks as completed
4. Delete completed tasks

Tasks are stored in a JSON file called 'tasks.json' so that the task list is saved even after the script exits.
The script uses functions for modularity and error handling for robustness.

Author: ChatGPT
Date: May 2025
"""

import json
import os

TASKS_FILE = 'tasks.json'


def load_tasks():
    """Load tasks from the JSON file or return an empty list if file doesn't exist."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    """Save the list of tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks, description):
    """Add a new task to the list."""
    task = {'description': description, 'completed': False}
    tasks.append(task)
    print(f"Task added: {description}")


def view_tasks(tasks):
    """Display all tasks with their status."""
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = 'Done' if task['completed'] else 'Pending'
        print(f"{idx}. {task['description']} [{status}]")


def mark_task_completed(tasks, index):
    """Mark a task as completed."""
    try:
        tasks[index]['completed'] = True
        print(f"Task marked as completed: {tasks[index]['description']}")
    except IndexError:
        print("Invalid task number.")


def delete_completed_tasks(tasks):
    """Remove all completed tasks from the list."""
    before_count = len(tasks)
    tasks[:] = [task for task in tasks if not task['completed']]
    removed = before_count - len(tasks)
    print(f"{removed} completed task(s) removed.")


def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Completed Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            desc = input("Enter task description: ")
            add_task(tasks, desc)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            view_tasks(tasks)
            try:
                idx = int(input("Enter task number to mark as completed: ")) - 1
                mark_task_completed(tasks, idx)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            delete_completed_tasks(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()


"""
OOP Task Manager Script

Description:
-------------
This Python script implements a simple task manager using Object-Oriented Programming (OOP).
It allows users to:
1. Add new tasks
2. View all tasks
3. Mark tasks as completed
4. Delete completed tasks

The script uses two main classes:
- Task: represents a single task
- TaskManager: manages the list of tasks, handles file operations, and provides menu options

Tasks are saved to and loaded from a JSON file ('tasks.json') to persist data across runs.

Author: ChatGPT
Date: May 2025
"""

import json
import os

TASKS_FILE = 'tasks.json'


class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {'description': self.description, 'completed': self.completed}

    @staticmethod
    def from_dict(data):
        return Task(data['description'], data['completed'])


class TaskManager:
    def __init__(self, file_path=TASKS_FILE):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return [Task.from_dict(item) for item in data]
        return []

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, description):
        self.tasks.append(Task(description))
        print(f"Task added: {description}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for idx, task in enumerate(self.tasks, 1):
            status = 'Done' if task.completed else 'Pending'
            print(f"{idx}. {task.description} [{status}]")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print(f"Task marked as completed: {self.tasks[index].description}")
        else:
            print("Invalid task number.")

    def delete_completed_tasks(self):
        before_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task.completed]
        removed = before_count - len(self.tasks)
        print(f"{removed} completed task(s) removed.")

    def run(self):
        while True:
            print("\nTask Manager Menu:")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Delete Completed Tasks")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                desc = input("Enter task description: ")
                self.add_task(desc)
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.view_tasks()
                try:
                    idx = int(input("Enter task number to mark as completed: ")) - 1
                    self.mark_task_completed(idx)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == '4':
                self.delete_completed_tasks()
            elif choice == '5':
                self.save_tasks()
                print("Tasks saved. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    manager = TaskManager()
    manager.run()




print("cassandra is pretty, but she's a rapist")
paul = "hello everyone"
print(paul)
num_one = 765
num_two = 677664


total = num_one + num_two
print(total)
user_name = input("what is your name: ")
print("welcome to UCU!!!",user_name)

Paul = "Handsome"
Yolo = "Cute"

Salim = "Funny"

print(Paul)

"""
Task Manager Script

Description:
-------------
This Python script is a simple command-line task manager that allows users to:
1. Add new tasks
2. View all tasks
3. Mark tasks as completed
4. Delete completed tasks

Tasks are stored in a JSON file called 'tasks.json' so that the task list is saved even after the script exits.
The script uses functions for modularity and error handling for robustness.

Author: ChatGPT
Date: May 2025
"""

import json
import os

TASKS_FILE = 'tasks.json'


def load_tasks():
    """Load tasks from the JSON file or return an empty list if file doesn't exist."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    """Save the list of tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks, description):
    """Add a new task to the list."""
    task = {'description': description, 'completed': False}
    tasks.append(task)
    print(f"Task added: {description}")


def view_tasks(tasks):
    """Display all tasks with their status."""
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = 'Done' if task['completed'] else 'Pending'
        print(f"{idx}. {task['description']} [{status}]")


def mark_task_completed(tasks, index):
    """Mark a task as completed."""
    try:
        tasks[index]['completed'] = True
        print(f"Task marked as completed: {tasks[index]['description']}")
    except IndexError:
        print("Invalid task number.")


def delete_completed_tasks(tasks):
    """Remove all completed tasks from the list."""
    before_count = len(tasks)
    tasks[:] = [task for task in tasks if not task['completed']]
    removed = before_count - len(tasks)
    print(f"{removed} completed task(s) removed.")


def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Completed Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            desc = input("Enter task description: ")
            add_task(tasks, desc)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            view_tasks(tasks)
            try:
                idx = int(input("Enter task number to mark as completed: ")) - 1
                mark_task_completed(tasks, idx)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            delete_completed_tasks(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()


"""
OOP Task Manager Script

Description:
-------------
This Python script implements a simple task manager using Object-Oriented Programming (OOP).
It allows users to:
1. Add new tasks
2. View all tasks
3. Mark tasks as completed
4. Delete completed tasks

The script uses two main classes:
- Task: represents a single task
- TaskManager: manages the list of tasks, handles file operations, and provides menu options

Tasks are saved to and loaded from a JSON file ('tasks.json') to persist data across runs.

Author: ChatGPT
Date: May 2025
"""

import json
import os

TASKS_FILE = 'tasks.json'


class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {'description': self.description, 'completed': self.completed}

    @staticmethod
    def from_dict(data):
        return Task(data['description'], data['completed'])


class TaskManager:
    def __init__(self, file_path=TASKS_FILE):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return [Task.from_dict(item) for item in data]
        return []

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, description):
        self.tasks.append(Task(description))
        print(f"Task added: {description}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for idx, task in enumerate(self.tasks, 1):
            status = 'Done' if task.completed else 'Pending'
            print(f"{idx}. {task.description} [{status}]")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print(f"Task marked as completed: {self.tasks[index].description}")
        else:
            print("Invalid task number.")

    def delete_completed_tasks(self):
        before_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task.completed]
        removed = before_count - len(self.tasks)
        print(f"{removed} completed task(s) removed.")

    def run(self):
        while True:
            print("\nTask Manager Menu:")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Delete Completed Tasks")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                desc = input("Enter task description: ")
                self.add_task(desc)
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.view_tasks()
                try:
                    idx = int(input("Enter task number to mark as completed: ")) - 1
                    self.mark_task_completed(idx)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == '4':
                self.delete_completed_tasks()
            elif choice == '5':
                self.save_tasks()
                print("Tasks saved. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    manager = TaskManager()
    manager.run()




print("cassandra is pretty, but she's a rapist")
paul = "hello everyone"
print(paul)
num_one = 765
num_two = 677664


total = num_one + num_two
print(total)
user_name = input("what is your name: ")
print("welcome to UCU!!!",user_name)

Paul = "Handsome"
Yolo = "Cute"

Salim = "Funny"

print(Paul)

"""
Task Manager Script

Description:
-------------
This Python script is a simple command-line task manager that allows users to:
1. Add new tasks
2. View all tasks
3. Mark tasks as completed
4. Delete completed tasks

Tasks are stored in a JSON file called 'tasks.json' so that the task list is saved even after the script exits.
The script uses functions for modularity and error handling for robustness.

Author: ChatGPT
Date: May 2025
"""

import json
import os

TASKS_FILE = 'tasks.json'


def load_tasks():
    """Load tasks from the JSON file or return an empty list if file doesn't exist."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    """Save the list of tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks, description):
    """Add a new task to the list."""
    task = {'description': description, 'completed': False}
    tasks.append(task)
    print(f"Task added: {description}")


def view_tasks(tasks):
    """Display all tasks with their status."""
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = 'Done' if task['completed'] else 'Pending'
        print(f"{idx}. {task['description']} [{status}]")


def mark_task_completed(tasks, index):
    """Mark a task as completed."""
    try:
        tasks[index]['completed'] = True
        print(f"Task marked as completed: {tasks[index]['description']}")
    except IndexError:
        print("Invalid task number.")


def delete_completed_tasks(tasks):
    """Remove all completed tasks from the list."""
    before_count = len(tasks)
    tasks[:] = [task for task in tasks if not task['completed']]
    removed = before_count - len(tasks)
    print(f"{removed} completed task(s) removed.")


def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Completed Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            desc = input("Enter task description: ")
            add_task(tasks, desc)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            view_tasks(tasks)
            try:
                idx = int(input("Enter task number to mark as completed: ")) - 1
                mark_task_completed(tasks, idx)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            delete_completed_tasks(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()


"""
OOP Task Manager Script

Description:
-------------
This Python script implements a simple task manager using Object-Oriented Programming (OOP).
It allows users to:
1. Add new tasks
2. View all tasks
3. Mark tasks as completed
4. Delete completed tasks

The script uses two main classes:
- Task: represents a single task
- TaskManager: manages the list of tasks, handles file operations, and provides menu options

Tasks are saved to and loaded from a JSON file ('tasks.json') to persist data across runs.

Author: ChatGPT
Date: May 2025
"""

import json
import os

TASKS_FILE = 'tasks.json'


class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {'description': self.description, 'completed': self.completed}

    @staticmethod
    def from_dict(data):
        return Task(data['description'], data['completed'])


class TaskManager:
    def __init__(self, file_path=TASKS_FILE):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return [Task.from_dict(item) for item in data]
        return []

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, description):
        self.tasks.append(Task(description))
        print(f"Task added: {description}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for idx, task in enumerate(self.tasks, 1):
            status = 'Done' if task.completed else 'Pending'
            print(f"{idx}. {task.description} [{status}]")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print(f"Task marked as completed: {self.tasks[index].description}")
        else:
            print("Invalid task number.")

    def delete_completed_tasks(self):
        before_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task.completed]
        removed = before_count - len(self.tasks)
        print(f"{removed} completed task(s) removed.")

    def run(self):
        while True:
            print("\nTask Manager Menu:")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Delete Completed Tasks")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                desc = input("Enter task description: ")
                self.add_task(desc)
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.view_tasks()
                try:
                    idx = int(input("Enter task number to mark as completed: ")) - 1
                    self.mark_task_completed(idx)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == '4':
                self.delete_completed_tasks()
            elif choice == '5':
                self.save_tasks()
                print("Tasks saved. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    manager = TaskManager()
    manager.run()




print("cassandra is pretty, but she's a rapist")
paul = "hello everyone"
print(paul)
num_one = 765
num_two = 677664


total = num_one + num_two
print(total)
user_name = input("what is your name: ")
print("welcome to UCU!!!",user_name)

Paul = "Handsome"
Yolo = "Cute"

Salim = "Funny"

print(Paul)

"""
Task Manager Script

Description:
-------------
This Python script is a simple command-line task manager that allows users to:
1. Add new tasks
2. View all tasks
3. Mark tasks as completed
4. Delete completed tasks

Tasks are stored in a JSON file called 'tasks.json' so that the task list is saved even after the script exits.
The script uses functions for modularity and error handling for robustness.

Author: ChatGPT
Date: May 2025
"""

import json
import os

TASKS_FILE = 'tasks.json'


def load_tasks():
    """Load tasks from the JSON file or return an empty list if file doesn't exist."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    """Save the list of tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks, description):
    """Add a new task to the list."""
    task = {'description': description, 'completed': False}
    tasks.append(task)
    print(f"Task added: {description}")


def view_tasks(tasks):
    """Display all tasks with their status."""
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = 'Done' if task['completed'] else 'Pending'
        print(f"{idx}. {task['description']} [{status}]")


def mark_task_completed(tasks, index):
    """Mark a task as completed."""
    try:
        tasks[index]['completed'] = True
        print(f"Task marked as completed: {tasks[index]['description']}")
    except IndexError:
        print("Invalid task number.")


def delete_completed_tasks(tasks):
    """Remove all completed tasks from the list."""
    before_count = len(tasks)
    tasks[:] = [task for task in tasks if not task['completed']]
    removed = before_count - len(tasks)
    print(f"{removed} completed task(s) removed.")


def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Completed Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            desc = input("Enter task description: ")
            add_task(tasks, desc)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            view_tasks(tasks)
            try:
                idx = int(input("Enter task number to mark as completed: ")) - 1
                mark_task_completed(tasks, idx)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            delete_completed_tasks(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()


"""
OOP Task Manager Script

Description:
-------------
This Python script implements a simple task manager using Object-Oriented Programming (OOP).
It allows users to:
1. Add new tasks
2. View all tasks
3. Mark tasks as completed
4. Delete completed tasks

The script uses two main classes:
- Task: represents a single task
- TaskManager: manages the list of tasks, handles file operations, and provides menu options

Tasks are saved to and loaded from a JSON file ('tasks.json') to persist data across runs.

Author: ChatGPT
Date: May 2025
"""

import json
import os

TASKS_FILE = 'tasks.json'


class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {'description': self.description, 'completed': self.completed}

    @staticmethod
    def from_dict(data):
        return Task(data['description'], data['completed'])


class TaskManager:
    def __init__(self, file_path=TASKS_FILE):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return [Task.from_dict(item) for item in data]
        return []

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, description):
        self.tasks.append(Task(description))
        print(f"Task added: {description}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for idx, task in enumerate(self.tasks, 1):
            status = 'Done' if task.completed else 'Pending'
            print(f"{idx}. {task.description} [{status}]")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print(f"Task marked as completed: {self.tasks[index].description}")
        else:
            print("Invalid task number.")

    def delete_completed_tasks(self):
        before_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task.completed]
        removed = before_count - len(self.tasks)
        print(f"{removed} completed task(s) removed.")

    def run(self):
        while True:
            print("\nTask Manager Menu:")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Delete Completed Tasks")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                desc = input("Enter task description: ")
                self.add_task(desc)
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.view_tasks()
                try:
                    idx = int(input("Enter task number to mark as completed: ")) - 1
                    self.mark_task_completed(idx)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == '4':
                self.delete_completed_tasks()
            elif choice == '5':
                self.save_tasks()
                print("Tasks saved. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    manager = TaskManager()
    manager.run()




print("cassandra is pretty, but she's a rapist")
paul = "hello everyone"
print(paul)
num_one = 765
num_two = 677664


total = num_one + num_two
print(total)
user_name = input("what is your name: ")
print("welcome to UCU!!!",user_name)

Paul = "Handsome"
Yolo = "Cute"

Salim = "Funny"

print(Paul)

"""
Task Manager Script

Description:
-------------
This Python script is a simple command-line task manager that allows users to:
1. Add new tasks
2. View all tasks
3. Mark tasks as completed
4. Delete completed tasks

Tasks are stored in a JSON file called 'tasks.json' so that the task list is saved even after the script exits.
The script uses functions for modularity and error handling for robustness.

Author: ChatGPT
Date: May 2025
"""

import json
import os

TASKS_FILE = 'tasks.json'


def load_tasks():
    """Load tasks from the JSON file or return an empty list if file doesn't exist."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    """Save the list of tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks, description):
    """Add a new task to the list."""
    task = {'description': description, 'completed': False}
    tasks.append(task)
    print(f"Task added: {description}")


def view_tasks(tasks):
    """Display all tasks with their status."""
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = 'Done' if task['completed'] else 'Pending'
        print(f"{idx}. {task['description']} [{status}]")


def mark_task_completed(tasks, index):
    """Mark a task as completed."""
    try:
        tasks[index]['completed'] = True
        print(f"Task marked as completed: {tasks[index]['description']}")
    except IndexError:
        print("Invalid task number.")


def delete_completed_tasks(tasks):
    """Remove all completed tasks from the list."""
    before_count = len(tasks)
    tasks[:] = [task for task in tasks if not task['completed']]
    removed = before_count - len(tasks)
    print(f"{removed} completed task(s) removed.")


def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Completed Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            desc = input("Enter task description: ")
            add_task(tasks, desc)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            view_tasks(tasks)
            try:
                idx = int(input("Enter task number to mark as completed: ")) - 1
                mark_task_completed(tasks, idx)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            delete_completed_tasks(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()


"""
OOP Task Manager Script

Description:
-------------
This Python script implements a simple task manager using Object-Oriented Programming (OOP).
It allows users to:
1. Add new tasks
2. View all tasks
3. Mark tasks as completed
4. Delete completed tasks

The script uses two main classes:
- Task: represents a single task
- TaskManager: manages the list of tasks, handles file operations, and provides menu options

Tasks are saved to and loaded from a JSON file ('tasks.json') to persist data across runs.

Author: ChatGPT
Date: May 2025
"""

import json
import os

TASKS_FILE = 'tasks.json'


class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {'description': self.description, 'completed': self.completed}

    @staticmethod
    def from_dict(data):
        return Task(data['description'], data['completed'])


class TaskManager:
    def __init__(self, file_path=TASKS_FILE):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return [Task.from_dict(item) for item in data]
        return []

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, description):
        self.tasks.append(Task(description))
        print(f"Task added: {description}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for idx, task in enumerate(self.tasks, 1):
            status = 'Done' if task.completed else 'Pending'
            print(f"{idx}. {task.description} [{status}]")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print(f"Task marked as completed: {self.tasks[index].description}")
        else:
            print("Invalid task number.")

    def delete_completed_tasks(self):
        before_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task.completed]
        removed = before_count - len(self.tasks)
        print(f"{removed} completed task(s) removed.")

    def run(self):
        while True:
            print("\nTask Manager Menu:")
            print("1. Add Task")
            print("2. View Tasks")
 




print("cassandra is pretty, but she's a rapist")
paul = "hello everyone"
print(paul)
num_one = 765
num_two = 677664


total = num_one + num_two
print(total)
user_name = input("what is your name: ")
print("welcome to UCU!!!",user_name)

Paul = "Handsome"
Yolo = "Cute"

Salim = "Funny"

print(Paul)

"""
Task Manager Script

Description:
-------------
This Python script is a simple command-line task manager that allows users to:
1. Add new tasks
2. View all tasks
3. Mark tasks as completed
4. Delete completed tasks

Tasks are stored in a JSON file called 'tasks.json' so that the task list is saved even after the script exits.
The script uses functions for modularity and error handling for robustness.

Author: ChatGPT
Date: May 2025
"""

import json
import os

TASKS_FILE = 'tasks.json'


def load_tasks():
    """Load tasks from the JSON file or return an empty list if file doesn't exist."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    """Save the list of tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks, description):
    """Add a new task to the list."""
    task = {'description': description, 'completed': False}
    tasks.append(task)
    print(f"Task added: {description}")


def view_tasks(tasks):
    """Display all tasks with their status."""
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = 'Done' if task['completed'] else 'Pending'
        print(f"{idx}. {task['description']} [{status}]")


def mark_task_completed(tasks, index):
    """Mark a task as completed."""
    try:
        tasks[index]['completed'] = True
        print(f"Task marked as completed: {tasks[index]['description']}")
    except IndexError:
        print("Invalid task number.")


def delete_completed_tasks(tasks):
    """Remove all completed tasks from the list."""
    before_count = len(tasks)
    tasks[:] = [task for task in tasks if not task['completed']]
    removed = before_count - len(tasks)
    print(f"{removed} completed task(s) removed.")


def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Completed Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            desc = input("Enter task description: ")
            add_task(tasks, desc)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            view_tasks(tasks)
            try:
                idx = int(input("Enter task number to mark as completed: ")) - 1
                mark_task_completed(tasks, idx)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            delete_completed_tasks(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()


"""
OOP Task Manager Script

Description:
-------------
This Python script implements a simple task manager using Object-Oriented Programming (OOP).
It allows users to:
1. Add new tasks
2. View all tasks
3. Mark tasks as completed
4. Delete completed tasks

The script uses two main classes:
- Task: represents a single task
- TaskManager: manages the list of tasks, handles file operations, and provides menu options

Tasks are saved to and loaded from a JSON file ('tasks.json') to persist data across runs.

Author: ChatGPT
Date: May 2025
"""

import json
import os

TASKS_FILE = 'tasks.json'


class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {'description': self.description, 'completed': self.completed}

    @staticmethod
    def from_dict(data):
        return Task(data['description'], data['completed'])


class TaskManager:
    def __init__(self, file_path=TASKS_FILE):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return [Task.from_dict(item) for item in data]
        return []

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, description):
        self.tasks.append(Task(description))
        print(f"Task added: {description}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for idx, task in enumerate(self.tasks, 1):
            status = 'Done' if task.completed else 'Pending'
            print(f"{idx}. {task.description} [{status}]")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print(f"Task marked as completed: {self.tasks[index].description}")
        else:
            print("Invalid task number.")

    def delete_completed_tasks(self):
        before_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task.completed]
        removed = before_count - len(self.tasks)
        print(f"{removed} completed task(s) removed.")

    def run(self):
        while True:
            print("\nTask Manager Menu:")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Delete Completed Tasks")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                desc = input("Enter task description: ")
                self.add_task(desc)
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.view_tasks()
                try:
                    idx = int(input("Enter task number to mark as completed: ")) - 1
                    self.mark_task_completed(idx)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == '4':
                self.delete_completed_tasks()
            elif choice == '5':
                self.save_tasks()
                print("Tasks saved. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    manager = TaskManager()
    manager.run()




print("cassandra is pretty, but she's a rapist")
paul = "hello everyone"
print(paul)
num_one = 765
num_two = 677664


total = num_one + num_two
print(total)
user_name = input("what is your name: ")
print("welcome to UCU!!!",user_name)

Paul = "Handsome"
Yolo = "Cute"

Salim = "Funny"

print(Paul)

"""
Task Manager Script

Description:
-------------
This Python script is a simple command-line task manager that allows users to:
1. Add new tasks
2. View all tasks
3. Mark tasks as completed
4. Delete completed tasks

Tasks are stored in a JSON file called 'tasks.json' so that the task list is saved even after the script exits.
The script uses functions for modularity and error handling for robustness.

Author: ChatGPT
Date: May 2025
"""

import json
import os

TASKS_FILE = 'tasks.json'


def load_tasks():
    """Load tasks from the JSON file or return an empty list if file doesn't exist."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    """Save the list of tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks, description):
    """Add a new task to the list."""
    task = {'description': description, 'completed': False}
    tasks.append(task)
    print(f"Task added: {description}")


def view_tasks(tasks):
    """Display all tasks with their status."""
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = 'Done' if task['completed'] else 'Pending'
        print(f"{idx}. {task['description']} [{status}]")


def mark_task_completed(tasks, index):
    """Mark a task as completed."""
    try:
        tasks[index]['completed'] = True
        print(f"Task marked as completed: {tasks[index]['description']}")
    except IndexError:
        print("Invalid task number.")


def delete_completed_tasks(tasks):
    """Remove all completed tasks from the list."""
    before_count = len(tasks)
    tasks[:] = [task for task in tasks if not task['completed']]
    removed = before_count - len(tasks)
    print(f"{removed} completed task(s) removed.")


def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Completed Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            desc = input("Enter task description: ")
            add_task(tasks, desc)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            view_tasks(tasks)
            try:
                idx = int(input("Enter task number to mark as completed: ")) - 1
                mark_task_completed(tasks, idx)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            delete_completed_tasks(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()


"""
OOP Task Manager Script

Description:
-------------
This Python script implements a simple task manager using Object-Oriented Programming (OOP).
It allows users to:
1. Add new tasks
2. View all tasks
3. Mark tasks as completed
4. Delete completed tasks

The script uses two main classes:
- Task: represents a single task
- TaskManager: manages the list of tasks, handles file operations, and provides menu options

Tasks are saved to and loaded from a JSON file ('tasks.json') to persist data across runs.

Author: ChatGPT
Date: May 2025
"""

import json
import os

TASKS_FILE = 'tasks.json'


class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {'description': self.description, 'completed': self.completed}

    @staticmethod
    def from_dict(data):
        return Task(data['description'], data['completed'])


class TaskManager:
    def __init__(self, file_path=TASKS_FILE):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return [Task.from_dict(item) for item in data]
        return []

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, description):
        self.tasks.append(Task(description))
        print(f"Task added: {description}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for idx, task in enumerate(self.tasks, 1):
            status = 'Done' if task.completed else 'Pending'
            print(f"{idx}. {task.description} [{status}]")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print(f"Task marked as completed: {self.tasks[index].description}")
        else:
            print("Invalid task number.")

    def delete_completed_tasks(self):
        before_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task.completed]
        removed = before_count - len(self.tasks)
        print(f"{removed} completed task(s) removed.")

    def run(self):
        while True:
            print("\nTask Manager Menu:")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Delete Completed Tasks")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                desc = input("Enter task description: ")
                self.add_task(desc)
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.view_tasks()
                try:
                    idx = int(input("Enter task number to mark as completed: ")) - 1
                    self.mark_task_completed(idx)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == '4':
                self.delete_completed_tasks()
            elif choice == '5':
                self.save_tasks()
                print("Tasks saved. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    manager = TaskManager()
    manager.run()




print("cassandra is pretty, but she's a rapist")
paul = "hello everyone"
print(paul)
num_one = 765
num_two = 677664


total = num_one + num_two
print(total)
user_name = input("what is your name: ")
print("welcome to UCU!!!",user_name)

Paul = "Handsome"
Yolo = "Cute"

Salim = "Funny"

print(Paul)

"""
Task Manager Script

Description:
-------------
This Python script is a simple command-line task manager that allows users to:
1. Add new tasks
2. View all tasks
3. Mark tasks as completed
4. Delete completed tasks

Tasks are stored in a JSON file called 'tasks.json' so that the task list is saved even after the script exits.
The script uses functions for modularity and error handling for robustness.

Author: ChatGPT
Date: May 2025
"""

import json
import os

TASKS_FILE = 'tasks.json'


def load_tasks():
    """Load tasks from the JSON file or return an empty list if file doesn't exist."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    """Save the list of tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks, description):
    """Add a new task to the list."""
    task = {'description': description, 'completed': False}
    tasks.append(task)
    print(f"Task added: {description}")


def view_tasks(tasks):
    """Display all tasks with their status."""
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = 'Done' if task['completed'] else 'Pending'
        print(f"{idx}. {task['description']} [{status}]")


def mark_task_completed(tasks, index):
    """Mark a task as completed."""
    try:
        tasks[index]['completed'] = True
        print(f"Task marked as completed: {tasks[index]['description']}")
    except IndexError:
        print("Invalid task number.")


def delete_completed_tasks(tasks):
    """Remove all completed tasks from the list."""
    before_count = len(tasks)
    tasks[:] = [task for task in tasks if not task['completed']]
    removed = before_count - len(tasks)
    print(f"{removed} completed task(s) removed.")


def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Completed Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            desc = input("Enter task description: ")
            add_task(tasks, desc)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            view_tasks(tasks)
            try:
                idx = int(input("Enter task number to mark as completed: ")) - 1
                mark_task_completed(tasks, idx)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            delete_completed_tasks(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()


"""
OOP Task Manager Script

Description:
-------------
This Python script implements a simple task manager using Object-Oriented Programming (OOP).
It allows users to:
1. Add new tasks
2. View all tasks
3. Mark tasks as completed
4. Delete completed tasks

The script uses two main classes:
- Task: represents a single task
- TaskManager: manages the list of tasks, handles file operations, and provides menu options

Tasks are saved to and loaded from a JSON file ('tasks.json') to persist data across runs.

Author: ChatGPT
Date: May 2025
"""

import json
import os

TASKS_FILE = 'tasks.json'


class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {'description': self.description, 'completed': self.completed}

    @staticmethod
    def from_dict(data):
        return Task(data['description'], data['completed'])


class TaskManager:
    def __init__(self, file_path=TASKS_FILE):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return [Task.from_dict(item) for item in data]
        return []

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, description):
        self.tasks.append(Task(description))
        print(f"Task added: {description}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for idx, task in enumerate(self.tasks, 1):
            status = 'Done' if task.completed else 'Pending'
            print(f"{idx}. {task.description} [{status}]")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print(f"Task marked as completed: {self.tasks[index].description}")
        else:
            print("Invalid task number.")

    def delete_completed_tasks(self):
        before_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task.completed]
        removed = before_count - len(self.tasks)
        print(f"{removed} completed task(s) removed.")

    def run(self):
        while True:
            print("\nTask Manager Menu:")
            print("1. Add Task")
            print("2. View Tasks")
 