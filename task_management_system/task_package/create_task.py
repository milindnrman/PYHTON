from .task import Task

def create_task(title,description,category=None):
    new_task=Task(title,description,category)
    return new_task