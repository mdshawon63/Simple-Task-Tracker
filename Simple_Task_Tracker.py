class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        title = input("Enter Title: ")
        description = input("Enter Description: ")

        task = {
            "title": title,
            "description": description
        }

        self.tasks.append(task)
        print("Task added successfully!\n")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.\n")
            return

        print("\n--- Your Tasks ---")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. Title: {task['title']}")
            print(f"   Description: {task['description']}\n")

    def delete_task(self):
        if not self.tasks:
            print("No tasks to delete.\n")
            return

        self.view_tasks()
        try:
            choice = int(input("Enter task number to delete: "))
            if 1 <= choice <= len(self.tasks):
                deleted = self.tasks.pop(choice - 1)
                print(f"Task '{deleted['title']}' deleted successfully!\n")
            else:
                print("Invalid task number.\n")
        except ValueError:
            print("Please enter a valid number.\n")

task_manager = TaskManager()

while True:
    print("===== Task Tracker =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task_manager.add_task()
    elif choice == "2":
        task_manager.view_tasks()
    elif choice == "3":
        task_manager.delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.\n")
        print("Wrong input\n")
