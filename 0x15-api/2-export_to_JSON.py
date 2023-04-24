#!/usr/bin/python3
"""This is a python script that export data in the JSON format."""


from sys import argv
import requests
import json


if __name__ == '__main__':
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
    tasks = task_response.json()


    output = {EMPLOYEE_ID: []}
    for task in tasks:
        output[EMPLOYEE_ID].append({
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_name
        })


    with open(f"{EMPLOYEE_ID}.json", "w") as f:
        json.dump(output, f)
