def get_next_id(tasks):
    if not tasks:
        return 1

    return max(task["id"] for task in tasks) + 1


def add_task(tasks, title):
    task = {
        "id": get_next_id(tasks),
        "title": title,
        "done": False
    }

    tasks.append(task)
    return task


def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\n=== Tasks ===")
    for i, task in enumerate(tasks, start=1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"{i}. {status} {task['title']}")


def delete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return True

    return False


def mark_task_done(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return True

    return False