# todo.py

# Function to manage a to-do list
to_do_list = []

def add_task(task):
    to_do_list.append(task)
    return f"Task added: {task}"

def view_tasks():
    return to_do_list if to_do_list else "To-do list is empty."

def remove_task(task):
    if task in to_do_list:
        to_do_list.remove(task)
        return f"Task removed: {task}"
    else:
        return "Task not found."

def update_task(old_task, new_task):
    if old_task in to_do_list:
        index = to_do_list.index(old_task)
        to_do_list[index] = new_task
        return f"Task updated: {old_task} to {new_task}"
    else:
        return "Task not found."
