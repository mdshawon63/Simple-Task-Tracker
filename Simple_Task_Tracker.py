class TaskManager:
    def __init__(self):
        self.tasks = [
            {"title": "Study Python", "description": "Finish basics and loops"},
            {"title": "Complete Assignment", "description": "Submit task tracker project"},
            {"title": "Exercise", "description": "30 minutes cardio"}
        ]

    def add_task(self):
        new_tasks = [
            {"title": "Learn JSON", "description": "Understand data storage"},
            {"title": "Read Book", "description": "Read 10 pages daily"}
        ]
        self.tasks.extend(new_tasks)
        print("Tasks added!")

    def view_tasks(self):
        print("\n--- Your Tasks ---")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task['title']} - {task['description']}")

    def delete_task(self):
        if self.tasks:
            removed = self.tasks.pop()
            print(f"Task '{removed['title']}' deleted!")
        else:
            print("No task to delete!")

    def run(self):
        print("Initial Tasks:")
        self.view_tasks()

        print("\nAdding Tasks...")
        self.add_task()
        self.view_tasks()

        print("\nDeleting Task...")
        self.delete_task()
    

TaskManager().run()