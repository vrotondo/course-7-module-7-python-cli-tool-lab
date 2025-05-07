# cli_tool.py

import argparse
try:
    from lib.models import Task, User
except ImportError:
    # Handle relative imports when running as a module
    from models import Task, User

# Global dictionary to store users and their tasks
users = {}

def add_task(args):
    """
    Add a task for a user
    
    Args:
        args: Command line arguments containing user and title
    """
    # Get the user or create a new one if they don't exist
    user = users.get(args.user)
    if not user:
        user = User(args.user)
        users[args.user] = user
    
    # Create and add the task
    task = Task(args.title)
    user.add_task(task)

def complete_task(args):
    """
    Mark a task as complete
    
    Args:
        args: Command line arguments containing user and title
    """
    user = users.get(args.user)
    if user:
        task = user.get_task_by_title(args.title)
        if task:
            task.complete()
        else:
            print(f"Task '{args.title}' not found for user {args.user}.")
    else:
        print(f"User '{args.user}' not found.")

def main():
    """Main entry point for the CLI tool"""
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # Subparser for adding tasks
    add_parser = subparsers.add_parser("add-task", help="Add a task for a user")
    add_parser.add_argument("user", help="Name of the user")
    add_parser.add_argument("title", help="Title of the task")
    add_parser.set_defaults(func=add_task)
    
    # Subparser for completing tasks
    complete_parser = subparsers.add_parser("complete-task", help="Complete a user's task")
    complete_parser.add_argument("user", help="Name of the user")
    complete_parser.add_argument("title", help="Title of the task to complete")
    complete_parser.set_defaults(func=complete_task)
    
    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()