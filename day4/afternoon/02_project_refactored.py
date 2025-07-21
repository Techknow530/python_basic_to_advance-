"""
Project 1 - Task Management System (Refactored)
==============================================

This is a refactored version of a task management system.
It demonstrates best practices for code organization, documentation, and structure.

Author: [Your Name]
Date: [Current Date]
Version: 2.0
"""

from datetime import datetime
from typing import List, Dict, Optional, Any
import json
import os


class TaskStatus:
    """Constants for task status values."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class TaskPriority:
    """Constants for task priority values."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class Task:
    """
    Represents a single task in the task management system.
    
    This class encapsulates all the properties and behaviors of a task,
    including creation, updating, and status management.
    """
    
    def __init__(self, title: str, description: str = "", priority: str = TaskPriority.MEDIUM):
        """
        Initialize a new task.
        
        Args:
            title (str): The title of the task
            description (str, optional): Detailed description of the task
            priority (str, optional): Priority level (low, medium, high, urgent)
        
        Raises:
            ValueError: If title is empty or priority is invalid
        """
        if not title.strip():
            raise ValueError("Task title cannot be empty")
        
        if priority not in [TaskPriority.LOW, TaskPriority.MEDIUM, 
                           TaskPriority.HIGH, TaskPriority.URGENT]:
            raise ValueError(f"Invalid priority: {priority}")
        
        self.id = self._generate_id()
        self.title = title.strip()
        self.description = description.strip()
        self.priority = priority
        self.status = TaskStatus.PENDING
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.completed_at = None
        self.tags = []
        self.due_date = None
    
    def _generate_id(self) -> str:
        """
        Generate a unique ID for the task.
        
        Returns:
            str: A unique identifier for the task
        """
        import uuid
        return str(uuid.uuid4())[:8]
    
    def update_status(self, new_status: str) -> None:
        """
        Update the task status.
        
        Args:
            new_status (str): The new status for the task
        
        Raises:
            ValueError: If the status is invalid
        """
        valid_statuses = [TaskStatus.PENDING, TaskStatus.IN_PROGRESS, 
                         TaskStatus.COMPLETED, TaskStatus.CANCELLED]
        
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}")
        
        old_status = self.status
        self.status = new_status
        self.updated_at = datetime.now()
        
        # Set completion time if task is completed
        if new_status == TaskStatus.COMPLETED:
            self.completed_at = datetime.now()
        elif old_status == TaskStatus.COMPLETED:
            self.completed_at = None
    
    def add_tag(self, tag: str) -> None:
        """
        Add a tag to the task.
        
        Args:
            tag (str): The tag to add
        """
        tag = tag.strip().lower()
        if tag and tag not in self.tags:
            self.tags.append(tag)
            self.updated_at = datetime.now()
    
    def remove_tag(self, tag: str) -> None:
        """
        Remove a tag from the task.
        
        Args:
            tag (str): The tag to remove
        """
        tag = tag.strip().lower()
        if tag in self.tags:
            self.tags.remove(tag)
            self.updated_at = datetime.now()
    
    def set_due_date(self, due_date: datetime) -> None:
        """
        Set the due date for the task.
        
        Args:
            due_date (datetime): The due date for the task
        """
        self.due_date = due_date
        self.updated_at = datetime.now()
    
    def is_overdue(self) -> bool:
        """
        Check if the task is overdue.
        
        Returns:
            bool: True if the task is overdue, False otherwise
        """
        if not self.due_date:
            return False
        
        if self.status in [TaskStatus.COMPLETED, TaskStatus.CANCELLED]:
            return False
        
        return datetime.now() > self.due_date
    
    def get_age_in_days(self) -> int:
        """
        Get the age of the task in days.
        
        Returns:
            int: Number of days since task creation
        """
        return (datetime.now() - self.created_at).days
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the task to a dictionary for serialization.
        
        Returns:
            Dict[str, Any]: Dictionary representation of the task
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'completed_at': self.completed_at.isoformat() if self.completed_at else None,
            'tags': self.tags,
            'due_date': self.due_date.isoformat() if self.due_date else None
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Task':
        """
        Create a task instance from a dictionary.
        
        Args:
            data (Dict[str, Any]): Dictionary containing task data
        
        Returns:
            Task: A new task instance
        """
        task = cls(data['title'], data['description'], data['priority'])
        task.id = data['id']
        task.status = data['status']
        task.created_at = datetime.fromisoformat(data['created_at'])
        task.updated_at = datetime.fromisoformat(data['updated_at'])
        
        if data['completed_at']:
            task.completed_at = datetime.fromisoformat(data['completed_at'])
        
        task.tags = data.get('tags', [])
        
        if data['due_date']:
            task.due_date = datetime.fromisoformat(data['due_date'])
        
        return task
    
    def __str__(self) -> str:
        """String representation of the task."""
        status_emoji = {
            TaskStatus.PENDING: "⏳",
            TaskStatus.IN_PROGRESS: "🔄",
            TaskStatus.COMPLETED: "✅",
            TaskStatus.CANCELLED: "❌"
        }
        
        priority_emoji = {
            TaskPriority.LOW: "🟢",
            TaskPriority.MEDIUM: "🟡",
            TaskPriority.HIGH: "🟠",
            TaskPriority.URGENT: "🔴"
        }
        
        return f"{status_emoji[self.status]} {priority_emoji[self.priority]} {self.title}"
    
    def __repr__(self) -> str:
        """Detailed representation of the task."""
        return f"Task(id={self.id}, title='{self.title}', status={self.status}, priority={self.priority})"


class TaskManager:
    """
    Manages a collection of tasks with CRUD operations and persistence.
    
    This class provides comprehensive task management functionality including
    creation, updating, searching, filtering, and file-based persistence.
    """
    
    def __init__(self, storage_file: str = "tasks.json"):
        """
        Initialize the task manager.
        
        Args:
            storage_file (str): Path to the JSON file for task persistence
        """
        self.storage_file = storage_file
        self.tasks: List[Task] = []
        self.load_tasks()
    
    def create_task(self, title: str, description: str = "", 
                   priority: str = TaskPriority.MEDIUM) -> Task:
        """
        Create a new task.
        
        Args:
            title (str): The title of the task
            description (str, optional): Detailed description
            priority (str, optional): Priority level
        
        Returns:
            Task: The newly created task
        
        Raises:
            ValueError: If task creation fails
        """
        task = Task(title, description, priority)
        self.tasks.append(task)
        self.save_tasks()
        return task
    
    def get_task(self, task_id: str) -> Optional[Task]:
        """
        Get a task by its ID.
        
        Args:
            task_id (str): The ID of the task to retrieve
        
        Returns:
            Optional[Task]: The task if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def update_task(self, task_id: str, **kwargs) -> bool:
        """
        Update a task's properties.
        
        Args:
            task_id (str): The ID of the task to update
            **kwargs: Properties to update
        
        Returns:
            bool: True if task was updated, False if not found
        """
        task = self.get_task(task_id)
        if not task:
            return False
        
        # Update allowed properties
        if 'title' in kwargs:
            task.title = kwargs['title'].strip()
        if 'description' in kwargs:
            task.description = kwargs['description'].strip()
        if 'priority' in kwargs:
            if kwargs['priority'] in [TaskPriority.LOW, TaskPriority.MEDIUM, 
                                    TaskPriority.HIGH, TaskPriority.URGENT]:
                task.priority = kwargs['priority']
        if 'status' in kwargs:
            task.update_status(kwargs['status'])
        if 'due_date' in kwargs:
            task.set_due_date(kwargs['due_date'])
        
        task.updated_at = datetime.now()
        self.save_tasks()
        return True
    
    def delete_task(self, task_id: str) -> bool:
        """
        Delete a task by its ID.
        
        Args:
            task_id (str): The ID of the task to delete
        
        Returns:
            bool: True if task was deleted, False if not found
        """
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            return True
        return False
    
    def list_tasks(self, status: Optional[str] = None, 
                  priority: Optional[str] = None,
                  tag: Optional[str] = None) -> List[Task]:
        """
        List tasks with optional filtering.
        
        Args:
            status (Optional[str]): Filter by status
            priority (Optional[str]): Filter by priority
            tag (Optional[str]): Filter by tag
        
        Returns:
            List[Task]: List of tasks matching the criteria
        """
        filtered_tasks = self.tasks
        
        if status:
            filtered_tasks = [t for t in filtered_tasks if t.status == status]
        
        if priority:
            filtered_tasks = [t for t in filtered_tasks if t.priority == priority]
        
        if tag:
            filtered_tasks = [t for t in filtered_tasks if tag.lower() in t.tags]
        
        return filtered_tasks
    
    def search_tasks(self, query: str) -> List[Task]:
        """
        Search tasks by title or description.
        
        Args:
            query (str): Search query
        
        Returns:
            List[Task]: List of tasks matching the search query
        """
        query = query.lower()
        matching_tasks = []
        
        for task in self.tasks:
            if (query in task.title.lower() or 
                query in task.description.lower() or
                query in ' '.join(task.tags)):
                matching_tasks.append(task)
        
        return matching_tasks
    
    def get_overdue_tasks(self) -> List[Task]:
        """
        Get all overdue tasks.
        
        Returns:
            List[Task]: List of overdue tasks
        """
        return [task for task in self.tasks if task.is_overdue()]
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Get task statistics.
        
        Returns:
            Dict[str, Any]: Dictionary containing various statistics
        """
        total_tasks = len(self.tasks)
        
        if total_tasks == 0:
            return {
                'total_tasks': 0,
                'by_status': {},
                'by_priority': {},
                'overdue_count': 0,
                'completion_rate': 0.0
            }
        
        status_counts = {}
        priority_counts = {}
        
        for task in self.tasks:
            status_counts[task.status] = status_counts.get(task.status, 0) + 1
            priority_counts[task.priority] = priority_counts.get(task.priority, 0) + 1
        
        completed_count = status_counts.get(TaskStatus.COMPLETED, 0)
        completion_rate = (completed_count / total_tasks) * 100
        
        return {
            'total_tasks': total_tasks,
            'by_status': status_counts,
            'by_priority': priority_counts,
            'overdue_count': len(self.get_overdue_tasks()),
            'completion_rate': completion_rate
        }
    
    def save_tasks(self) -> None:
        """Save tasks to the storage file."""
        try:
            data = [task.to_dict() for task in self.tasks]
            with open(self.storage_file, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def load_tasks(self) -> None:
        """Load tasks from the storage file."""
        if not os.path.exists(self.storage_file):
            return
        
        try:
            with open(self.storage_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(task_data) for task_data in data]
        except Exception as e:
            print(f"Error loading tasks: {e}")
            self.tasks = []
    
    def __len__(self) -> int:
        """Return the number of tasks."""
        return len(self.tasks)
    
    def __str__(self) -> str:
        """String representation of the task manager."""
        return f"TaskManager({len(self.tasks)} tasks)"


# Example usage and testing
if __name__ == "__main__":
    # Create task manager
    tm = TaskManager("sample_tasks.json")
    
    # Create sample tasks
    task1 = tm.create_task("Complete project proposal", 
                          "Write and submit the project proposal for Q1",
                          TaskPriority.HIGH)
    
    task2 = tm.create_task("Review code", 
                          "Review pull requests from team members",
                          TaskPriority.MEDIUM)
    
    task3 = tm.create_task("Update documentation", 
                          "Update API documentation with new endpoints",
                          TaskPriority.LOW)
    
    # Add tags
    task1.add_tag("work")
    task1.add_tag("urgent")
    task2.add_tag("development")
    task3.add_tag("documentation")
    
    # Update task status
    tm.update_task(task2.id, status=TaskStatus.IN_PROGRESS)
    
    # Display tasks
    print("All tasks:")
    for task in tm.list_tasks():
        print(f"  {task}")
    
    # Display statistics
    print(f"\nStatistics: {tm.get_statistics()}")
    
    # Search tasks
    results = tm.search_tasks("project")
    print(f"\nSearch results for 'project': {len(results)} tasks found")
    
    print("\nTask management system demonstration complete!")
