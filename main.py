import datetime

tasks = []

def add_task():
    print("\n--- Add a New Task ---")
    title = input("Task name: ")
    deadline_str = input("Deadline (YYYY-MM-DD): ")

    try:
        deadline = datetime.datetime.strptime(deadline_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Task not added.")
        return
    
    task = {
        "title": title,
        "deadline": deadline,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("\nNo tasks yet.")
        return

    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Not done"
        print(f"{i}. {task['title']} | Deadline: {task['deadline']} | Status: {status}")

def mark_completed():
    view_tasks()
    if not tasks:
        return

    try:
        num = int(input("\nEnter task number to mark complete: "))
        tasks[num - 1]["completed"] = True
        print("Task marked as completed!")
    except (ValueError, IndexError):
        print("Invalid choice.")

def show_due_soon():
    print("\n--- Tasks Due Soon (Next 3 Days) ---")
    today = datetime.date.today()
    found = False

    for task in tasks:
        if 0 <= (task["deadline"] - today).days <= 3 and not task["completed"]:
            print(f"- {task['title']} | Deadline: {task['deadline']}")
            found = True
    
    if not found:
        print("No urgent tasks!")

def main_menu():
    while True:
        print("\n-------------------------------------")
        print("       PERSONAL ORGANIZER APP")
        print("-------------------------------------")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Show Tasks Due Soon")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            show_due_soon()
        elif choice == "5":
            print("Goodbye! Stay productive 🙂")
            break
        else:
            print("Invalid input. Try again.")

main_menu()