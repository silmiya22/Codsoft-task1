
tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "done": False})

    elif choice == "2":
        for i, t in enumerate(tasks):
            status = "✓" if t["done"] else "✗"
            print(f"{i+1}. [{status}] {t['task']}")

    elif choice == "3":
        num = int(input("Task number to mark complete: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]["done"] = True

    elif choice == "4":
        num = int(input("Task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            tasks.pop(num)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
