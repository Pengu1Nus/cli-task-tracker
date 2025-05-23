from colorama import Fore, Style, init

from commands import process_command

init(autoreset=True)


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
