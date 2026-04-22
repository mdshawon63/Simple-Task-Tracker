class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        title = input("Title: ")
        desc = input("Description: ")
        self.tasks.append({"title": title, "description": desc})
        print("Task Added\n")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks\n")
            return

        for i, task in enumerate(self.tasks, 1):
            print(i, "-", task["title"], ":", task["description"])
        print()

    def delete_task(self):
        self.view_tasks()
        if not self.tasks:
            return

        num = int(input("Delete task number: "))
        if 1 <= num <= len(self.tasks):
            self.tasks.pop(num - 1)
            print("Task Deleted\n")
        else:
            print("Invalid number\n")


tm = TaskManager()

while True:
    print("1.Add  2.View  3.Delete  4.Exit")
    choice = input("Choice: ")

    if choice == "1":
        tm.add_task()
    elif choice == "2":
        tm.view_tasks()
    elif choice == "3":
        tm.delete_task()
    elif choice == "4":
        break
    else:
        print("Wrong input\n")
