
import argparse
import json
import os

def get_arguments():
    parser = argparse.ArgumentParser(description="CLI To-Do List App")
    parser.add_argument("action", choices=["add", "delete", "view"], help="Action to perform")
    parser.add_argument("--task", type=str, help="The task to add/delete")
    parser.add_argument("--id", type=int, help="The task ID to delete")
    return parser.parse_args()

def load_tasks(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=2)

def add_task(task, filename):
    tasks = load_tasks(filename)
    tasks.append(task)
    save_tasks(tasks, filename)
    print(f"Task '{task}' added.")

def delete_task(task_id, filename):
    tasks = load_tasks(filename)
    if 0 <= task_id < len(tasks):
        removed_task = tasks.pop(task_id)
        save_tasks(tasks, filename)
        print(f"Task '{removed_task}' deleted.")
    else:
        print(f"Task ID {task_id} does not exist.")

def view_tasks(filename):
    tasks = load_tasks(filename)
    for i, task in enumerate(tasks):
        print(f"{i}. {task}")

def main():
    args = get_arguments()
    filename = "tasks.json"

    if args.action == "add" and args.task:
        add_task(args.task, filename)
    elif args.action == "delete" and args.id is not None:
        delete_task(args.id, filename)
    elif args.action == "view":
        view_tasks(filename)
    else:
        print("Invalid command or missing parameters.")

if __name__ == "__main__":
    main()