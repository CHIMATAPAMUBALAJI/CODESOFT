# To-Do List Application

# Store tasks as a list of dictionaries
tasks = []

# Function to add a new task
def add_task():
    task_name = input("Enter the task: ")
    tasks.append({"task": task_name, "completed": False})
    print("Task added successfully!")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    print("\nTo-Do List:")
    for idx, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{idx}. {task['task']} - {status}")

# Function to update a task
def update_task():
    view_tasks()
    task_num = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_num < len(tasks):
        new_task = input("Enter the new task description: ")
        tasks[task_num]["task"] = new_task
        print("Task updated successfully!")
    else:
        print("Invalid task number.")

# Function to mark a task as completed
def mark_task_completed():
    view_tasks()
    task_num = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task():
    view_tasks()
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

# Main menu
def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            mark_task_completed()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()