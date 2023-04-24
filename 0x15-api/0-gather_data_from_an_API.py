#!/usr/bin/python3
"""A python script that for a given employee id, returns information about his /her TODO list progress"""

import requests
from sys import argv

if __name__ == "__main__":
    """Check if argument 2 is present"""
    if len(argv) != 2:
        print(f"Usage: {argv[0]} EMPLOYEE_ID")
        sys.exit(1)
    EMPLOYEE_ID = argv[1]
    API_URL = "https://jsonplaceholder.typicode.com"
    employee_response = requests.get(f"{API_URL}/users/{EMPLOYEE_ID}")
    employee_response.raise_for_status()
    employee_name = employee_response.json()["name"]
    task_response = requests.get(f"{API_URL}/todos?userId={EMPLOYEE_ID}")
    task_response.raise_for_status()
    task = task_response.json()
    total_tasks = len(task)
    done_tasks = len([todo for todo in task if todo["completed"]])

    print(f"Eployee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
    for todo in task:
        if todo["completed"]:
            print(f"\t{todo['title']}")
