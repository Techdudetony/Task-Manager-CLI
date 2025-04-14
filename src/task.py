# Defines the Task class with attributes and seriaalization logic

class Task:
    def __init__(self, id, title, due_date=None, priority="Low", completed=False):
        # Unique task ID, title, due date, priority level, and completion status
        self.id = id
        self.title = title
        self.due_date = due_date
        self.priority= priority
        self.completed= completed
        
    def to_dict(self):
        '''Convert the task object to a dictionary for JSON serialization'''
        return {
            "id": self.id,
            "title": self.title,
            "due_date": self.due_date,
            "priority": self.priority,
            "completed": self.completed
        }
        
    @staticmethod
    def from_dict(data):
        '''Create a Task object from a disctionary (used when loading from JSON)'''
        return Task(
            id=data["id"],
            title=data["title"],
            due_date=data.get("due_date"),
            priority=data.get("priority", "Low"),
            completed=data.get("completed", False)
        )
        
    def __str__(self):
        '''Return a formatted string representation of the task.'''
        return f"[{'✔' if self.completed else ' '}] {self.id}: {self.title} (Priority: {self.priority}, Due: {self.due_date})"