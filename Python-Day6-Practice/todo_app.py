tasks = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    while True:
        show_menu()

        choice = input("Enter your choice:")

        if choice == "1":
            task = input("Enter task: ")
            task.append(task)
            print("Task added!")

        elif choice == "2":
            if len(tasks) == 0:
                print("No Tasks found.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("No tasks to remove.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}.{task}")

                num = int(input("Enter task number to remove."))

                if 1 <= num <= len(tasks):
                    removed = task.pop(num -1)
                    print("Removed:", removed)
                else:
                    print("Invalid task number.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")
