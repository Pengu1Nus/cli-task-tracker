import json
from datetime import datetime


def add_task(task_description):
    current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    try:
        with open('data.json', 'r') as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    new_id = tasks[-1]['id'] + 1 if tasks else 1
    new_task = {
        'id': new_id,
        'description': ' '.join(task_description),
        'status': 'todo',
        'createdAt': current_time,
        'updatedAt': current_time,
    }
    tasks.append(new_task)

    with open('data.json', 'w') as file:
        json.dump(tasks, file, indent=4)

    print(f'Task added successfully (ID: {new_task["id"]})')


def update_task_description(task_id, task_description):
    task_description = ' '.join(task_description)
    try:
        with open('data.json', 'r') as file:
            tasks = json.load(file)
            found = False
            for elem in tasks:
                if elem['id'] == int(task_id):
                    elem['description'] = task_description
                    found = True
                    print('Task updated successfully')
                    break
            if not found:
                print('Task not found')
            with open('data.json', 'w') as file:
                json.dump(tasks, file, indent=4)

    except (FileNotFoundError, json.JSONDecodeError):
        print('Task not found')


def update_task_status(command, task_id):
    command = command[5:]

    try:
        with open('data.json', 'r') as file:
            tasks = json.load(file)
            found = False
            for elem in tasks:
                if elem['id'] == int(task_id):
                    elem['status'] = command
                    print('Task status updated successfully')
                    found = True
                    break
            if not found:
                print('Task not found')

            with open('data.json', 'w') as file:
                json.dump(tasks, file, indent=4)

    except (FileNotFoundError, json.JSONDecodeError):
        print('Task not found')


def delete_task(task_id):
    task_id = int(task_id[0])
    try:
        with open('data.json', 'r') as file:
            tasks = json.load(file)
            found = False
            for elem in tasks:
                if elem['id'] == task_id:
                    tasks.remove(elem)
                    found = True
                    print('Task deleted successfully')
                    break
            if not found:
                print('Task not found')
            with open('data.json', 'w') as file:
                json.dump(tasks, file, indent=4)
    except (FileNotFoundError, json.JSONDecodeError):
        print('Task not found')


def list_tasks(*argument):
    command = argument[0]
    try:
        with open('data.json', 'r') as file:
            tasks = json.load(file)
            if len(command) == 0:
                for task in tasks:
                    print(task)
            elif len(command) == 1:
                if command[0] == 'done':
                    for task in tasks:
                        if command[0] == task['status']:
                            print(task)
                if command[0] == 'todo':
                    for task in tasks:
                        if command[0] == task['status']:
                            print(task)
                if command[0] == 'in-progress':
                    for task in tasks:
                        if command[0] == task['status']:
                            print(task)
    except (FileNotFoundError, json.JSONDecodeError):
        print('There is no tasks yet')


def main():
    user_input = ''
    while user_input != 'logout':
        user_input = input('task-cli ').strip()
        command, *other = user_input.split()

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
