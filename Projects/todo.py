tasks = []

def display_menu():
    print("\n=== ToDo List Manager===")
    print("1. Add a task")
    print("2. View task")
    print("3. Mark task as done")
    print("4. Remove a task")
    print("5. Exit")

def add_task():
    task_name = input("Enter task name: ")
    tasks.append({"task" : task_name, "done" : False})
    print("Task added!")

def view_task():
    if not tasks:
        print("No tasks found!")
        return
    print("\nYour tasks: ")
    for i, task in enumerate(tasks, start=1):
        status = "[x]" if task["done"] else "[ ]" #if task["done"] == True:...
        print(f"{i}. {status} {task['task']}")

def mark_task():
    view_task()
    try:
        task_num = int(input("Enter the task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["done"] = True
            print("Task marked as done")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number")


def remove_task():
    view_task()
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Removed task: {removed['task']}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Enter a valid number.")

while True:
    display_menu()
    choice = int(input("Choose an option (1-5): "))

    if choice == 1:
        add_task()
    elif choice == 2:
        view_task()
    elif choice == 3:
        mark_task()
    elif choice == 4:
        remove_task()
    elif choice == 5:
        print("GoodBye!")
        break
    else:
        print("invalid option.")