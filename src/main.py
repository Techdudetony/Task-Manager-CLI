# Entry point for the Task Manager CLI using argparse for command handling

import argparse
from .task import Task
from .storage import load_tasks, save_tasks
from .utils import sort_tasks, PRIORITY_LEVELS

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest="command")
    
    # 'add' command
    add = subparsers.add_parser("add", help="Add a new task")
    add.add_argument("title", help="Task Title")
    add.add_argument("--priority", choices=PRIORITY_LEVELS, default="Low", help="Task Priority")
    add.add_argument("--due", help="Due date")
    
    # 'list' command
    list_tasks = subparsers.add_parser("list", help="List all tasks")
    list_tasks.add_argument("--sort", choices=["priority", "due_date"], help="Sort tasks")
    
    # 'complete' command
    complete = subparsers.add_parser("complete", help="Mark a task as complete")
    complete.add_argument("id", type=int, help="Task ID to complete")
    
    # 'delete' command
    delete = subparsers.add_parser("delete", help="Delete a task by ID")
    delete.add_argument("id", type=int, help="Task ID to delete")
    
    # Parse command-like arguments
    args = parser.parse_args()
    tasks = load_tasks()
    
    # Handle each command
    if args.command == "add":
        new_id = max([t.id for t in tasks], default=0) + 1
        new_task = Task(new_id, args.title, args.due, args.priority)
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"✅ Added task {new_task}")
        
    elif args.command == "list":
        sorted_tasks = sort_tasks(tasks, args.sort) if args.sort else tasks
        if not sorted_tasks:
            print("No tasks found.")
        for task in sorted_tasks:
            print(task)
            
    elif args.command == "complete":
        for task in tasks:
            if task.id == args.id:
                task.completed = True
                print(f"✅ Task marked complete {task}")
            else:
                print(f"❌ Task with ID {args.id} not found.")
        save_tasks(tasks)
        
    elif args.command == "delete":
        tasks = [task for task in tasks if task.id != args.id]
        save_tasks(tasks)
        print(f"Deleted task with ID {args.id}")
        
    else:
        parser.print_help()
        
if __name__ == "__main__":
    main()