#!/usr/bin/python3
"""This is a python script that export data into JSON format"""



import  requests
import json


API_URL ="https://jsonplaceholder.typicode.com"


employees_response = requests.get(f"{API_URL}/users")
employees_response.raise_for_status()
employees = employees_response.json()


tasks = {}


for employee in employees:
    employee_id = employee["id"]
    employee_name = employee["name"]


    task_response = requests.get(f"{API_URL}/todos?userId={employee_id}")
    task_response.raise_for_status()
    employee_tasks = task_response.json()


    task_list = []
    for task in employee_tasks:
        task_dict = {
                "username": employee_name,
                "task": task["title"],
                "completed": task["completed"]
        }
        task_list.append(task_dict)


    tasks[employee_id] = task_list


with open("todo_all_employees.json", "w") as file:
    json.dump(tasks, file)
