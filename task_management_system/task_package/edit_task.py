from .task import Task

def edit_task(task,new_title=None,new_description=None,new_category=None):
    if new_title:
        task.title=new_title
    if new_description:
        task.description=new_description
    if new_category:
        task.category=new_category