import json
import shutil


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
