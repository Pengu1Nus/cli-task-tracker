from colorama import Fore


def validate_task_id(task_id):
    """Validate the task ID and return the integer value."""
    try:
        return int(task_id)
    except ValueError:
        print(Fore.RED + 'Invalid task ID. Please provide a valid integer.')
        return None
