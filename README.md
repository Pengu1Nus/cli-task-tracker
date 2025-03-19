# Task CLI

Task CLI is a simple command-line task manager that allows users to add, update, delete, and manage tasks. The tasks are stored in a `data.json`.

## Features
- Add tasks
- Update task descriptions
- Delete tasks
- Mark tasks as "in progress", "done", or "todo"
- List all tasks or filter by status (todo, in-progress, done)

## Installation
1. Clone the repository:
   ```sh
   git clone git@github.com:Pengu1Nus/cli-task-tracker.git
   ```
   ```sh
   cd cli-task-tracker
   ```
2. Create and activate a virtual environment:
      - For Windows:
         - Createa virtual environment:
         ```sh
         python -m venv venv
         ```
         - Activate the virtual environment:
         ```sh
         .\venv\Scripts\activate
         ```
      - For macOS/Linux:
         - Create a virtual environment:
         ```sh
         python3 -m venv venv
         ```
         - Activate the virtual environment:
         ```sh
         source venv/bin/activate
         ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the CLI:
   ```sh
   python main.py
   ```

## Usage
### Adding a Task
```sh
task-cli > add Buy groceries
```
Output:
```sh
Task added successfully (ID: 1)
```

### Updating a Task
```sh
task-cli > update 1 Buy groceries and cook dinner
```
Output:
```sh
Task updated successfully
```

### Deleting a Task
```sh
task-cli > delete 1
```
Output:
```sh
Task deleted successfully
```

### Marking a Task as In Progress
```sh
task-cli > mark-in-progress 1
```
Output:
```sh
Task status updated successfully
```

### Marking a Task as Done
```sh
task-cli > mark-done 1
```
Output:
```sh
Task status updated successfully
```

### Listing All Tasks
```sh
task-cli > list
```

### Listing Tasks by Status
```sh
task-cli > list done
```
```sh
task-cli > list todo
```
```sh
task-cli > list in-progress
```

### Exiting the Program
```sh
task-cli > exit
```
