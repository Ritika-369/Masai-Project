import os
from datetime import datetime

TASKS_FILE = "tasks.txt"

# Helper function to load tasks from the file
def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            for line in file:
                task_id, description, deadline, status = line.strip().split(",")
                tasks.append({
                    "id": int(task_id),
                    "description": description,
                    "deadline": deadline,
                    "status": status
                })
    return tasks

# Helper function to save tasks to the file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task['id']},{task['description']},{task['deadline']},{task['status']}\n")

# Function to display tasks
def display_tasks(tasks):
    print("\nTo-Do List:")
    print("[Pending]")
    pending_tasks = [task for task in tasks if task["status"] == "Pending"]
    if pending_tasks:
        for task in pending_tasks:
            print(f"{task['id']}. {task['description']} - Deadline: {task['deadline']}")
    else:
        print("No pending tasks.")

    print("\n[Completed]")
    completed_tasks = [task for task in tasks if task["status"] == "Completed"]
    if completed_tasks:
        for task in completed_tasks:
            print(f"{task['id']}. {task['description']} - Deadline: {task['deadline']}")
    else:
        print("No tasks completed yet.")

# Function to add a task
def add_task(tasks):
    description = input("Enter task description: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    try:
        datetime.strptime(deadline, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
    task_id = max([task["id"] for task in tasks], default=0) + 1
    tasks.append({
        "id": task_id,
        "description": description,
        "deadline": deadline,
        "status": "Pending"
    })
    save_tasks(tasks)
    print("Task added successfully!")

# Function to edit a task
def edit_task(tasks):
    display_tasks(tasks)
    task_id = int(input("Enter the task ID to edit: "))
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = input("Enter new task description: ")
            task["deadline"] = input("Enter new deadline (YYYY-MM-DD): ")
            try:
                datetime.strptime(task["deadline"], "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                return
            save_tasks(tasks)
            print("Task updated successfully!")
            return
    print("Task not found.")

# Function to delete a task
def delete_task(tasks):
    display_tasks(tasks)
    task_id = int(input("Enter the task ID to delete: "))
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully!")
            return
    print("Task not found.")

# Function to mark a task as completed
def mark_task_completed(tasks):
    display_tasks(tasks)
    task_id = int(input("Enter the task ID to mark as completed: "))
    for task in tasks:
        if task["id"] == task_id:
            if task["status"] == "Completed":
                print("Task is already marked as completed.")
                return
            task["status"] = "Completed"
            save_tasks(tasks)
            print("Task marked as completed!")
            return
    print("Task not found.")

# Main program loop
def main():
    tasks = load_tasks()
    while True:
        print("\nWelcome to To-Do List Manager!")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            mark_task_completed(tasks)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
