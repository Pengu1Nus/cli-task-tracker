from datetime import datetime

from colorama import Fore, Style
from tabulate import tabulate

from file_operations import open_file, write_to_file
from utils import validate_task_id


def add_task(description):
    """Add a new task to the list."""
    current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    tasks = open_file()
    new_id = tasks[-1]['id'] + 1 if tasks else 1
    new_task = {
        'id': new_id,
        'description': description,
        'status': 'todo',
        'createdAt': current_time,
        'updatedAt': current_time,
    }
    tasks.append(new_task)
    write_to_file(tasks)
    print(Fore.GREEN + f'Task added successfully (ID: {new_task["id"]})')


def update_task(task_id, description):
    """Update the task description."""
    task_id = validate_task_id(task_id)
    if task_id is None:
        return

    current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    tasks = open_file()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            task['updatedAt'] = current_time
            write_to_file(tasks)
            print(Fore.GREEN + 'Task updated successfully')
            return
    print(Fore.RED + 'Task with given ID not found')


def update_task_status(task_id, status):
    """Update the task status."""
    task_id = validate_task_id(task_id)
    if task_id is None:
        return

    current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    tasks = open_file()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = current_time
            write_to_file(tasks)
            print(Fore.GREEN + 'Task status updated successfully')
            return
    print(Fore.RED + 'Task with given ID not found')


def delete_task(task_id):
    """Delete the task."""
    task_id = validate_task_id(task_id)
    if task_id is None:
        return

    tasks = open_file()
    updated_tasks = [task for task in tasks if task['id'] != task_id]
    if len(updated_tasks) == len(tasks):
        print(Fore.RED + 'Task with given ID not found')
        return
    write_to_file(updated_tasks)
    print(Fore.GREEN + 'Task deleted successfully')


def list_tasks(status=None):
    """List all tasks or tasks with a specific status."""
    valid_statuses = {'todo', 'done', 'in-progress'}

    if status and status not in valid_statuses:
        print(Fore.RED + 'Invalid status. Use: todo, done, or in-progress.')
        return

    tasks = open_file()
    headers = ('ID', 'Description', 'Status')

    if status:
        tasks = [task for task in tasks if task['status'] == status]

    task_list = []
    for task in tasks:
        status_color = {
            'todo': Fore.MAGENTA,
            'in-progress': Fore.YELLOW,
            'done': Fore.GREEN,
        }.get(task['status'], Fore.WHITE)
        task_list.append(
            [
                str(task['id']),
                task['description'],
                status_color + task['status'] + Style.RESET_ALL,
            ]
        )

    print(tabulate(task_list, headers=headers, tablefmt='pretty'))
