import json
import shutil
from datetime import datetime

from colorama import Fore, Style, init
from tabulate import tabulate

init(autoreset=True)


def open_file():
    """Open the file and return the tasks list."""

    try:
        with open('data.json', 'r') as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    return tasks


def write_to_file(tasks):
    """Write the tasks to the file."""

    try:
        with open('data.json', 'w') as file:
            json.dump(tasks, file, indent=4)
        shutil.copy('data.json', 'data_backup.json')
    except IOError as e:
        print(f'Error writing to file: {e}')


def validate_task_id(task_id):
    """Validate the task ID and return the integer value."""

    try:
        return int(task_id)
    except ValueError:
        print(Fore.RED + 'Invalid task ID. Please provide a valid integer.')
        return None


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
        if task['id'] == int(task_id):
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
        if task['id'] == int(task_id):
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
    updated_tasks = [task for task in tasks if task['id'] != int(task_id)]
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


def process_command(command, args):
    """Process the command and call the appropriate function."""

    def invalid():
        print(Fore.RED + 'Invalid command or arguments')

    def add():
        if args:
            add_task(' '.join(args))
        else:
            print(Fore.MAGENTA + 'Usage: add <task description>')

    def update():
        if len(args) > 1:
            update_task(args[0], ' '.join(args[1:]))
        else:
            print(Fore.MAGENTA + 'Usage: update <task_id> <new description>')

    def delete():
        if len(args) == 1:
            delete_task(args[0])
        else:
            print(Fore.MAGENTA + 'Usage: delete <task_id>')

    def mark_in_progress():
        if len(args) == 1:
            update_task_status(args[0], 'in-progress')
        else:
            print(Fore.MAGENTA + 'Usage: mark-in-progress <task_id>')

    def mark_done():
        if len(args) == 1:
            update_task_status(args[0], 'done')
        else:
            print(Fore.MAGENTA + 'Usage: mark-done <task_id>')

    def mark_todo():
        if len(args) == 1:
            update_task_status(args[0], 'todo')
        else:
            print(Fore.MAGENTA + 'Usage: mark-todo <task_id>')

    def list_tasks_command():
        list_tasks(args[0] if args else None)

    def exit_command():
        exit('Goodbye!')

    commands = {
        'add': add,
        'update': update,
        'delete': delete,
        'mark-in-progress': mark_in_progress,
        'mark-done': mark_done,
        'mark-todo': mark_todo,
        'list': list_tasks_command,
        'exit': exit_command,
    }

    commands.get(command, invalid)()


def main():
    """Main function to run the task-cli."""

    while True:
        user_input = input(
            Fore.YELLOW + 'task-cli > ' + Style.RESET_ALL
        ).strip()

        if not user_input:
            continue
        parts = user_input.split()
        command, args = parts[0], parts[1:]
        process_command(command, args)


if __name__ == '__main__':
    main()
