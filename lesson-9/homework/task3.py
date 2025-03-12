import json

def load_tasks(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

def save_tasks(file_name, tasks):
    with open(file_name, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    print("\nTasks:")
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

def calculate_statistics(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task['priority'] for task in tasks) / total_tasks if total_tasks > 0 else 0
    
    stats = {
        "Total Tasks": total_tasks,
        "Completed Tasks": completed_tasks,
        "Pending Tasks": pending_tasks,
        "Average Priority": round(average_priority, 2)
    }
    return stats

def update_task(tasks, task_id, completed=None, priority=None):
    for task in tasks:
        if task['id'] == task_id:
            if completed is not None:
                task['completed'] = completed
            if priority is not None:
                task['priority'] = priority
            return task
    return None

tasks_data = [
    {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
    {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
    {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
]

with open('tasks.json', 'w') as file:
    json.dump(tasks_data, file, indent=4)
tasks = load_tasks('tasks.json')
display_tasks(tasks)

stats = calculate_statistics(tasks)
print("\nTask Statistics:")
for key, value in stats.items():
    print(f"{key}: {value}")
update_task(tasks, task_id=3, completed=True)

save_tasks('tasks.json', tasks)
print("\nTask updated and saved back to tasks.json.")
