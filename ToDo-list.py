def Task():
    tasks = []

    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")
        choice = 0
        choice = int(input("Enter your choice: "))
        if choice == 1:
            try:
                n_tasks = int(input("How many tasks do you want to add: "))
                for i in range(n_tasks):
                    task = input(f"Enter task {i+1}: ")
                    tasks.append({"task": task, "done": False})
                    print(f"Task {i+1} added!")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == 2:
            print("\nTasks:")
            if not tasks:
                print("Your to-do list is empty.")
            else:
                for index, task in enumerate(tasks):
                    status = "Done" if task["done"] else "Not Done"
                    print(f"{index + 1}. {task['task']} - {status}")
        elif choice == 3:
            try:
                print("Enter task number to mark as done: ", end='')
                task_index = int(input()) - 1
                if 0 <= task_index < len(tasks):
                    tasks[task_index]["done"] = True
                    print("\nTask marked as done!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == 4:
            print("Exiting the To-Do List.")
            break
        else:
            print("Invalid choice. Please try again.")
#new function
print("hi this before call")
Task()
