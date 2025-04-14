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
    
    # 'list' command
    list_tasks = subparsers.add_parser("list", help="List all tasks")
    list_tasks.add_argument("--sort", choices=["priority", "due_date"], help="Sort tasks")
    
    # 'complete' command
    complete = subparsers.add_parser("complete", help="Mark a task as complete")
    complete.add_argument("id", type=int, help="Task ID to complete")
    
    # 'delete' command
    delete = subparsers.add_parser("delete", help="Delete a task by ID")
    delete.add_argument("id", type=int, help="Task ID to delete")
    
    # 'edit' command
    edit = subparsers.add_parser("edit", help="Edit a task by ID")
    edit.add_argument("id", type=int, help="Task ID to edit")
    
    # Parse command-like arguments
    args = parser.parse_args()
    tasks = load_tasks()
    
    # Handle each command
    if args.command == "add":
        print("Add a New Task")
        
        title = input("Enter task title: ").strip()
        while not title:
            title = input("Title cannot be empty. Please enter a task title: ").strip()
        
        priority = input("Enter priority level [Critical, High, Medium, Low]: ").strip().capitalize()
        while priority not in ["Critical", "High", "Medium", "Low"]:
            priority = input("Invalid priority. Choose from Critical, High, Medium, Low: ").strip().capitalize()
            
        due_date = input("Enter due date (YYYY-MM-DD): ").strip()
        if due_date == "":
            due_date = None
            
        tag = input("Enter tag (optional): ").strip()
        if tag == "":
            tag = None
            
        new_id = max([t.id for t in tasks], default=0) + 1
        new_task = Task(new_id, title, due_date, priority, tag=tag)
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"✅ Task added: {new_task}")
        
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
        
    elif args.command == "edit":
        found=False
        for task in tasks:
            found=True
            print(f"Editing Task: {task}")
            
            # Prompt user for updated fields
            new_title = input(f"New title (Leave blank to keep '{task.title}'): ") or task.title
            new_due = input(f"New due date (Leave blank to keep '{task.due_date}'): ") or task.due_date
            new_priority = input(f"New priority [Critical, High, Medium, Low] (Leave blank to keep '{task.priority}'): ") or task.priority
            
            # Update task
            task.title = new_title
            task.due_date = new_due
            task.priority = new_priority
            print(f"✅ Task updated: {task}")
            break
        if not found:
            print(f"❌ Task with ID {args.id} not found.")
        else:
            save_tasks(tasks)
        
    else:
        parser.print_help()
        
if __name__ == "__main__":
    main()