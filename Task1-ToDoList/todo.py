import json

# List to store tasks
tasks = []

# Function to add a task
def add_task():
    print("\n--- Add a Task ---")
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    task_id = len(tasks) + 1
    task = {
        "id": task_id,
        "title": title,
        "description": description,
        "deadline": deadline,
        "status": "pending"
    }
    tasks.append(task)
    print(f"Task '{title}' added successfully!\n")

# Function to view tasks
def view_tasks():
    print("\n--- View Tasks ---")
    if not tasks:
        print("No tasks available.\n")
        return
    for task in tasks:
        print(f"ID: {task['id']}")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Deadline: {task['deadline']}")
        print(f"Status: {task['status']}")
        print("-" * 30)
    print()

# Function to update a task
def update_task():
    print("\n--- Update a Task ---")
    if not tasks:
        print("No tasks available to update.\n")
        return
    view_tasks()
    task_id = input("Enter the task ID to update: ")
    for task in tasks:
        if str(task['id']) == task_id:
            print(f"\nEditing Task: {task['title']}")
            print("1. Mark as Completed")
            print("2. Edit Title")
            print("3. Edit Description")
            print("4. Edit Deadline")
            choice = input("Enter your choice: ")
            if choice == "1":
                task['status'] = "completed"
                print(f"Task '{task['title']}' marked as completed.\n")
            elif choice == "2":
                task['title'] = input("Enter new title: ")
                print(f"Title updated to '{task['title']}'.\n")
            elif choice == "3":
                task['description'] = input("Enter new description: ")
                print(f"Description updated.\n")
            elif choice == "4":
                task['deadline'] = input("Enter new deadline (YYYY-MM-DD): ")
                print(f"Deadline updated to {task['deadline']}.\n")
            else:
                print("Invalid choice. Returning to menu.\n")
            return
    print("Task ID not found.\n")

# Function to delete a task
def delete_task():
    print("\n--- Delete a Task ---")
    if not tasks:
        print("No tasks available to delete.\n")
        return
    view_tasks()
    task_id = input("Enter the task ID to delete: ")
    for task in tasks:
        if str(task['id']) == task_id:
            tasks.remove(task)
            print(f"Task '{task['title']}' deleted successfully.\n")
            return
    print("Task ID not found.\n")

# Function to save tasks to a file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    print("Tasks saved successfully!\n")

# Function to load tasks from a file
def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        print("Tasks loaded successfully!\n")
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
        print("No saved tasks found. Starting fresh.\n")


# Main menu
def main():
    load_tasks()
    while True:
        print("To-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Save and Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            save_tasks()
            print("Exiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Entry point for the program
if __name__ == "__main__":
    main()
