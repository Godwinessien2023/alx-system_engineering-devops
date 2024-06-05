#!/usr/bin/python3
import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    define get employee
    """
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Error fetching user data: {user_response.status_code}")
        return

    user_data = user_response.json()
    employee_name = user_data.get('name')


    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Error fetching todos data: {todos_response.status_code}")
        return

    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task['completed']]
    number_of_done_tasks = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("The employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
