tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added task: {task}")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Removed task: {task}")
    else:
        print(f"Task not found: {task}")

def show_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Your tasks:")
        for task in tasks:
            print(f"- {task}")

while True:
    print("\n1. Add Task\n2. Remove Task\n3. Show Tasks\n4. Exit")
    choice = input("Choose an option: ")
    
    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        show_tasks()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
