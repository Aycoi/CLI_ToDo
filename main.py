import argparse
import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(text):
    tasks = load_tasks()
    tasks.append({"text": text})
    save_tasks(tasks)
    print(f"Added task: {text}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['text']}")


def update_task(number, text):
    tasks = load_tasks()
    if not tasks:
        print("No tasks to update.")
        return
    idx = number or 1
    if idx < 1 or idx > len(tasks):
        print("Invalid task number.")
        return
    tasks[idx - 1]['text'] = text
    save_tasks(tasks)
    print(f"Updated task {idx}.")


def main():
    parser = argparse.ArgumentParser(description="Simple CLI ToDo manager")
    subparsers = parser.add_subparsers(dest="action", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("text", help="Task description")

    subparsers.add_parser("list", help="List all tasks")

    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("number", nargs="?", type=int, default=None, help="Task number to update")
    update_parser.add_argument("text", help="New task description")

    args = parser.parse_args()

    if args.action == "add":
        add_task(args.text)
    elif args.action == "list":
        list_tasks()
    elif args.action == "update":
        update_task(args.number, args.text)


if __name__ == "__main__":
    main()
