#!/usr/bin/python3
"""
A python script that for a given employee id,
returns information about his /her TODO list progress
"""

from sys import argv
import requests

if __name__ == "__main__":
    """Check if argument 2 is present"""
    if len(argv) != 2:
        print(f"Usage: {argv[0]} EMPLOYEE_ID")
        sys.exit(1)
    employee_id = argv[1]
    api_url = "https://jsonplaceholder.typicode.com"

    """Employees name"""
    employee_response = requests.get(f"{api_id}/users/{employee_id}")
    employee_response.raise_for_status()
    employee_name = employee_response.json()["name"]

    """The employees task list"""
    task_response = requests.get(f"{api_url}/todos?userId={employee_id}")
    task_response.raise_for_status()
    tasks = task_response.json()

    """Calculation of task list progress"""
    total_tasks = len(tasks)
    completed_tasks = [task for task in tasks if task["completed"]]
    completed_task_count = len(completed_tasks)

    """Print the progress report"""
    print(f"Employee {employee_name} is done with tasks"
          f"({completed_task_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")
