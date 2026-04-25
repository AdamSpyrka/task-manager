# CLI Task Manager

Simple command-line task manager written in Python.

## Features

- Add new tasks
- Display task list
- Mark tasks as completed
- Delete tasks
- Persistent storage using JSON

## How it works

Tasks are stored in a local `tasks.json` file and persist between program runs.
Each task includes an ID, title, and completion status.

Each task contains:
- unique ID
- title
- completion status

Tasks remain saved after closing and restarting the program.

## Example
````
=== Task Manager ===
1. Add task
2. Show tasks
3. Mark task as done
4. Delete task
5. Exit
Choose an option: 1
Enter task title: Study Python
Added task: Study Python

=== Task Manager ===
1. Add task
2. Show tasks
3. Mark task as done
4. Delete task
5. Exit
Choose an option: 2

=== Tasks ===
1. [ ] Study Python
````
## Technologies

- Python 3
- JSON (file-based storage)
- Standard library

## Project structure
````
task-manager/
├── main.py
├── task_manager.py
├── storage.py
├── tasks.json
├── README.md
└── .gitignore
````
## How to run
````
python main.py
````
## Notes

This project demonstrates:
- modular code structure
- file-based data persistence
- basic CRUD operations
- input validation
- separation of storage, logic, and interface
