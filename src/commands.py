from colorama import Fore
from task_operations import (
    add_task,
    delete_task,
    list_tasks,
    update_task,
    update_task_status,
)


def process_command(command, args):
    """Process the command and call the appropriate function."""

    command_handlers = {
        'add': lambda: add_task(' '.join(args))
        if args
        else print(Fore.MAGENTA + 'Usage: add <task description>'),
        'update': lambda: update_task(args[0], ' '.join(args[1:]))
        if len(args) > 1
        else print(Fore.MAGENTA + 'Usage: update <task_id> <new description>'),
        'delete': lambda: delete_task(args[0])
        if len(args) == 1
        else print(Fore.MAGENTA + 'Usage: delete <task_id>'),
        'mark-in-progress': lambda: update_task_status(args[0], 'in-progress')
        if len(args) == 1
        else print(Fore.MAGENTA + 'Usage: mark-in-progress <task_id>'),
        'mark-done': lambda: update_task_status(args[0], 'done')
        if len(args) == 1
        else print(Fore.MAGENTA + 'Usage: mark-done <task_id>'),
        'mark-todo': lambda: update_task_status(args[0], 'todo')
        if len(args) == 1
        else print(Fore.MAGENTA + 'Usage: mark-todo <task_id>'),
        'list': lambda: list_tasks(args[0] if args else None),
        'exit': lambda: exit('Goodbye!'),
    }

    command_handlers.get(
        command, lambda: print(Fore.RED + 'Invalid command or arguments')
    )()
