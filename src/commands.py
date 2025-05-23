from colorama import Fore

from task_operations import (
    add_task,
    delete_task,
    list_tasks,
    update_task,
    update_task_status,
)


def handle_add(args):
    if not args:
        print(Fore.MAGENTA + 'Usage: add <task description>')
        return
    add_task(' '.join(args))


def handle_update(args):
    if len(args) < 2:
        print(Fore.MAGENTA + 'Usage: update <task_id> <new description>')
        return
    update_task(args[0], ' '.join(args[1:]))


def handle_delete(args):
    if len(args) != 1:
        print(Fore.MAGENTA + 'Usage: delete <task_id>')
        return
    delete_task(args[0])


def handle_mark_status(args, status):
    if len(args) != 1:
        print(Fore.MAGENTA + f'Usage: mark-{status} <task_id>')
        return
    update_task_status(args[0], status)


def handle_list(args):
    list_tasks(args[0] if args else None)


def handle_exit(_):
    exit('Goodbye!')


def handle_invalid(_):
    print(Fore.RED + 'Invalid command or arguments')


def process_command(command, args):
    command_map = {
        'add': handle_add,
        'update': handle_update,
        'delete': handle_delete,
        'mark-in-progress': lambda args: handle_mark_status(
            args, 'in-progress'
        ),
        'mark-done': lambda args: handle_mark_status(args, 'done'),
        'mark-todo': lambda args: handle_mark_status(args, 'todo'),
        'list': handle_list,
        'exit': handle_exit,
    }

    command_map.get(command, handle_invalid)(args)
