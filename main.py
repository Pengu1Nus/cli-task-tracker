import json
from datetime import datetime

from tabulate import tabulate


def open_file():
    try:
        with open('data.json', 'r') as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    return tasks


def write_to_file(tasks):
    with open('data.json', 'w') as file:
        json.dump(tasks, file, indent=4)


def add_task(task_description):
    current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    task_description = ' '.join(task_description)
    tasks = open_file()
    new_id = tasks[-1]['id'] + 1 if tasks else 1
    new_task = {
        'id': new_id,
        'description': task_description,
        'status': 'todo',
        'createdAt': current_time,
        'updatedAt': current_time,
    }
    tasks.append(new_task)

    write_to_file(tasks)

    print(f'Task added successfully (ID: {new_task["id"]})')


def update_task_description(task_id, task_description):
    current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    task_description = ' '.join(task_description)

    found = False
    tasks = open_file()
    for elem in tasks:
        if elem['id'] == int(task_id):
            elem['description'] = task_description
            elem['updatedAt'] = current_time
            found = True
            print('Task updated successfully')
            break
    if not found:
        print('Task not found')

    write_to_file(tasks)


def update_task_status(command, task_id):
    current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    command = command[5:]
    tasks = open_file()

    found = False
    for elem in tasks:
        if elem['id'] == int(task_id):
            elem['status'] = command
            elem['updatedAt'] = current_time
            print('Task status updated successfully')
            found = True
            break
    if not found:
        print('Task not found')

    write_to_file(tasks)


def delete_task(task_id):
    # TODO: Implement if passing non-integer task_id

    try:
        task_id = int(task_id[0])
    except ValueError:
        print('Please, provide correct task ID')
        return

    tasks = open_file()

    found = False
    for elem in tasks:
        if elem['id'] == task_id:
            tasks.remove(elem)
            found = True
            print('Task deleted successfully')
            break
    if not found:
        print('Task not found')

    write_to_file(tasks)


def list_tasks(*argument):
    command = argument[0]
    if command not in ('done', 'todo', 'in-progress'):
        print('Invalid command')
        print('Available commands with list: done, todo, in-progress')
        return

    headers = {
        'id': 'ID',
        'description': 'Description',
        'status': 'Status',
    }
    tasks = open_file()

    if len(command) == 0:
        filtered_tasks = [
            {key: task[key] for key in ['id', 'description', 'status']}
            for task in tasks
        ]

        print(tabulate(filtered_tasks, headers=headers, tablefmt='pretty'))
    elif len(command) == 1:
        if command[0] == 'done':
            filtered_tasks = [
                {key: task[key] for key in ['id', 'description', 'status']}
                for task in tasks
                if command[0] == task['status']
            ]
            print(tabulate(filtered_tasks, headers=headers, tablefmt='pretty'))
        if command[0] == 'todo':
            filtered_tasks = [
                {key: task[key] for key in ['id', 'description', 'status']}
                for task in tasks
                if command[0] == task['status']
            ]
            print(tabulate(filtered_tasks, headers=headers, tablefmt='pretty'))
        if command[0] == 'in-progress':
            filtered_tasks = [
                {key: task[key] for key in ['id', 'description', 'status']}
                for task in tasks
                if command[0] == task['status']
            ]
            print(tabulate(filtered_tasks, headers=headers, tablefmt='pretty'))


def main():
    user_input = ''
    while user_input != 'logout':
        user_input = input('task-cli ').strip()
        command, *other = user_input.split()
        if command not in (
            'add',
            'update',
            'delete',
            'list',
            'mark',
            'logout',
        ):
            print('Invalid command')
            print(
                'Available commands: add, update, delete, list, mark, logout'
            )
        if command == 'logout':
            print('Bye!')
            break
        if command == 'add':
            task_description = other
            if task_description:
                add_task(task_description)
            else:
                print('Please, provide task description')
        if command == 'update':
            task_id, *task_description = other
            if task_id and task_description:
                update_task_description(task_id, task_description)
            else:
                print('Please, provide correct task data')
        if command == 'delete':
            if other:
                task_id = other
                delete_task(task_id)
            else:
                print('Please, provide task ID to delete')
        if command == 'list':
            list_tasks(other)
        if command.startswith('mark'):
            task_id = other[0]
            update_task_status(command, task_id)


if __name__ == '__main__':
    main()
