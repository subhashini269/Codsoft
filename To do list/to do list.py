import sys

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append({'description': description, 'completed': False})
        print(f"Task added: {description}")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks to do.")
            return
        print("\nTask List:")
        for index, task in enumerate(self.tasks, start=1):
            status = 'Completed' if task['completed'] else 'Pending'
            print(f"{index}. {task['description']} - {status}")

    def edit_task(self, task_number, new_description):
        if 1 <= task_number <= len(self.tasks):
            original_description = self.tasks[task_number - 1]['description']
            self.tasks[task_number - 1]['description'] = new_description
            print(f"Task updated: '{original_description}' to '{new_description}'")
        else:
            print("Task number is out of range.")

    def complete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]['completed'] = True
            print(f"Task {task_number} marked as completed.")
        else:
            print("Task number is out of range.")

    def remove_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            deleted_task = self.tasks.pop(task_number - 1)
            print(f"Removed task: {deleted_task['description']}")
        else:
            print("Task number is out of range.")

    def clear_all_tasks(self):
        self.tasks.clear()
        print("All tasks have been removed.")

def show_menu():
    print("""
Task Manager Application
-------------------------
1. Add a Task
2. View Tasks
3. Edit a Task
4. Mark Task as Completed
5. Remove a Task
6. Clear All Tasks
7. Exit
""")

def run_application():
    manager = TaskManager()

    while True:
        show_menu()
        choice = input("Select an option: ").strip()

        if choice == '1':
            description = input("Enter task description: ").strip()
            manager.add_task(description)
        elif choice == '2':
            manager.display_tasks()
        elif choice == '3':
            manager.display_tasks()
            try:
                task_number = int(input("Enter the task number to edit: ").strip())
                new_description = input("Enter new task description: ").strip()
                manager.edit_task(task_number, new_description)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '4':
            manager.display_tasks()
            try:
                task_number = int(input("Enter the task number to mark as completed: ").strip())
                manager.complete_task(task_number)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '5':
            manager.display_tasks()
            try:
                task_number = int(input("Enter the task number to remove: ").strip())
                manager.remove_task(task_number)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '6':
            manager.clear_all_tasks()
        elif choice == '7':
            print("Exiting Task Manager. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    run_application()
