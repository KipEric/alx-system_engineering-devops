#!/usr/bin/python3
"""Python script to export data in the CSV format."""


import csv
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2:
        print(f"Usage: {argv[0]} EMPLOYEE_ID")
        sys.exit(1)


    EMPLOYEE_ID = argv[1]
    API_URL = "https://jsonplaceholder.typicode.com"


    employee_response = requests.get(f"{API_URL}/users/{EMPLOYEE_ID}")
    employee_response.raise_for_status()
    employee_name = employee_response.json()["username"]


    task_response = requests.get(f"{API_URL}/todos?userId={EMPLOYEE_ID}")
    task_response.raise_for_status()
    tasks = task_response.json()


    filename = f"{EMPLOYEE_ID}.csv"


    with open(filename, mode='w') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()


        for task in tasks:
            writer.writerow({
                'USER_ID': EMPLOYEE_ID,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': task['completed'],
                'TASK_TITLE': task['title']
            })


    print(f"Data expected to {filename}")
