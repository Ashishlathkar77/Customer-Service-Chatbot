# Function to manage a to-do list
to_do_list = []

def manage_todo_list(action, task=None, task_to_update=None):
    if action == "add":
        if task:
            to_do_list.append(task)
            return f"Task added: {task}"
        else:
            return "No task provided."
    elif action == "view":
        return "\n".join(to_do_list) if to_do_list else "To-do list is empty."
    elif action == "remove":
        if task in to_do_list:
            to_do_list.remove(task)
            return f"Task removed: {task}"
        else:
            return "Task not found."
    elif action == "update":
        if task in to_do_list and task_to_update:
            index = to_do_list.index(task)
            to_do_list[index] = task_to_update
            return f"Task updated: {task} to {task_to_update}"
        else:
            return "Task not found or no new task provided."
    else:
        return "Invalid action."
