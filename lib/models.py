# models.py

class Task:
    def __init__(self, title):
        """
        Initialize a new Task with a title
        
        Args:
            title (str): The name/description of the task
        """
        self.title = title
        self.completed = False
    
    def complete(self):
        """Mark the task as completed and print confirmation"""
        self.completed = True
        print(f"Task '{self.title}' completed.")


class User:
    def __init__(self, name):
        """
        Initialize a new User with a name
        
        Args:
            name (str): The name of the user
        """
        self.name = name
        self.tasks = []
    
    def add_task(self, task):
        """
        Add a task to the user's task list
        
        Args:
            task (Task): The task to add
        """
        self.tasks.append(task)
        print(f"Task '{task.title}' added to {self.name}.")
    
    def get_task_by_title(self, title):
        """
        Find a task by its title
        
        Args:
            title (str): The title of the task to find
            
        Returns:
            Task or None: The found task or None if not found
        """
        for task in self.tasks:
            if task.title == title:
                return task
        return None