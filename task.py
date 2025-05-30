from enum import Enum
from datetime import datetime

class TaskStatus(Enum):
    TODO = "To Do"
    IN_PROGRESS = "In Progress"
    DONE = "Done"

class Task:
    _id_counter = 1 
    
    def __init__(self, description="", status=TaskStatus.TODO):
        self.id = Task._id_counter
        Task._id_counter += 1
        
        self.description = description
        self.created_at = datetime.now()
        self.updated_at = None
        self.status = status
        
    def set_description(self, description):
        self.updated_at = datetime.now()
        self.description = description

    def set_in_progress(self):
        self.updated_at = datetime.now()
        self.status = TaskStatus.IN_PROGRESS

    def set_done(self):
        self.updated_at = datetime.now()
        self.status = TaskStatus.DONE

    def set_todo(self):
        self.updated_at = datetime.now()
        self.status = TaskStatus.TODO
        
    def get_details(self):
        # Put the lines in separate indicies for readability
        lines = [
            f"Description: {self.description if self.description else 'None'}",
            f"    Status: {self.status.value} - Created: {self.created_at.strftime('%m/%d/%Y %I:%M %p') if self.created_at else 'No due date'} - Updated: {self.updated_at.strftime('%m/%d/%Y %I:%M %p') if self.updated_at else 'Not updated'} - Task ID: {self.id}"
        ]
        return "\n".join(lines)


    def __str__(self):
        created = self.created_at.strftime("%m/%d/%Y %I:%M %p") if self.created_at else 'No due date'
        updated = self.updated_at.strftime("%m/%d/%Y %I:%M %p") if self.updated_at else 'Not updated'
        return f"Task('{self.title}', Status: {self.status.value}, Created: {created}, Updated: {updated}, ID: {self.id})"
