from task_package.create_task import create_task
from task_package.edit_task import edit_task
from task_package.categorize_task import category_task

# create task 

task1=create_task("Complete your Assigment","Finish TASK MANAGEMNET SYSTEM")

print("Task1:",task1)

# edit task

edit_task(task1,new_title="Updated Assigement",new_description="Review and submit to Rashmi Mam")

# Display updated task 
print("Updated Task:",task1)

# categorize task 
category_task(task1,"Zappcode Academy")

# Disaplay category task 

print("Categorized Task1:",task1)