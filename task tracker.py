import argparse
import json
import os

# File where the tasks will be stored
TODO_FILE = 'todo.json'

# Ensure the file exists
def init_file():
    if not os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'w') as f:
            json.dump([], f)

# Load tasks from JSON file
def load_tasks():
    with open(TODO_FILE, 'r') as f:
        return json.load(f)

# Save tasks to JSON file
def save_tasks(tasks):
    with open(TODO_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# Add a new task
def add_task(description):
    tasks = load_tasks()
    tasks.append({"task": description, "completed": False})
    save_tasks(tasks)
    print(f"Added task: '{description}'")

# List all tasks
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. {task['task']} [{status}]")

# Delete a task by index
def delete_task(index):
    tasks = load_tasks()
    try:
        task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Deleted task: '{task['task']}'")
    except IndexError:
        print("Invalid task number.")

# Mark a task as complete by index
def complete_task(index):
    tasks = load_tasks()
    try:
        tasks[index - 1]['completed'] = True
        save_tasks(tasks)
        print(f"Completed task: '{tasks[index - 1]['task']}'")
    except IndexError:
        print("Invalid task number.")

# Command-line argument parsing
def main():
    parser = argparse.ArgumentParser(description="To-Do List CLI App")
    
    parser.add_argument('action', choices=['add', 'list', 'delete', 'complete'], 
                        help="Action to perform: add, list, delete, complete")
    parser.add_argument('value', nargs='?', help="Task description or task number")
    
    args = parser.parse_args()

    init_file()

    if args.action == 'add':
        if args.value:
            add_task(args.value)
        else:
            print("Please provide a task description to add.")
    elif args.action == 'list':
        list_tasks()
    elif args.action == 'delete':
        if args.value and args.value.isdigit():
            delete_task(int(args.value))
        else:
            print("Please provide a valid task number to delete.")
    elif args.action == 'complete':
        if args.value and args.value.isdigit():
            complete_task(int(args.value))
        else:
            print("Please provide a valid task number to complete.")

if __name__ == "__main__":
    main()
