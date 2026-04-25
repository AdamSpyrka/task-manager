from storage import load_tasks, save_tasks
from task_manager import add_task, list_tasks, delete_task, mark_task_done


def show_menu():
    print("\n=== Task Manager ===")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")


def get_task_id():
    while True:
        try:
            return int(input("Enter task ID: "))
        except ValueError:
            print("Invalid number. Try again.")


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Enter task title: ").strip()

            if not title:
                print("Task cannot be empty.")
                continue

            task = add_task(tasks, title)
            save_tasks(tasks)
            print(f"Added task: {task['title']}")

        elif choice == "2":
            list_tasks(tasks)

        elif choice == "3":
            list_tasks(tasks)
            index = get_task_id() - 1

            if index < 0 or index >= len(tasks):
                print("Task not found.")
                continue

            task_id = tasks[index]["id"]

            if mark_task_done(tasks, task_id):
                save_tasks(tasks)
                print("Task marked as done.")
            else:
                print("Task not found.")

        elif choice == "4":
            list_tasks(tasks)
            index = get_task_id() - 1

            if index < 0 or index >= len(tasks):
                print("Task not found.")
                continue

            task_id = tasks[index]["id"]

            if delete_task(tasks, task_id):
                save_tasks(tasks)
                print("Task deleted.")
            else:
                print("Task not found.")

        elif choice == "5":
            print("Goodbye.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()