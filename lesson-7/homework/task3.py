import json

class ToDoApp:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def add_task(self):
        task = {
            "id": input("Task ID: "),
            "title": input("Title: "),
            "description": input("Description: "),
            "status": input("Status (Pending/In Progress/Completed): ")
        }
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ")
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        print("Task deleted successfully!")

    def menu(self):
        while True:
            choice = input("1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit\nEnter choice: ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.delete_task()
            elif choice == "4":
                self.save_tasks()
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    ToDoApp().menu()
