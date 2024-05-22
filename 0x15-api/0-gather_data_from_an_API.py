#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""
# https://jsonplaceholder.typicode.com
import requests
import sys

if __name__ == "__main__":

    employee_id = sys.argv[1]
    user = requests.get(
        "https://jsonplaceholder.typicode./users/{}".format(employee_id)
    )

    name = user.json.get("name")

    todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    totalTask = 0
    completed = 0
    
    for task in todo.json():
        if task.get('userId') == int(employee_id):
            totalTask += 1
            if task.get('completed'):
                completed += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totalTask))

    print('\n'.join(["\t " + task.get('title') for task in todo.json()
          if task.get('userId') == int(employee_id) and task.get('completed')]))
