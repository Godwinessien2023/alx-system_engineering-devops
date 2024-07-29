#!/usr/bin/python3
import requests
import sys

def get_employee_todo_list(employee_id):
    # Base URL for the REST API
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Get employee details
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        return
    
    user = user_response.json()
    employee_name = user.get("name")
    
    # Get employee's TODO list
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    if todos_response.status_code != 200:
        print(f"Could not retrieve TODO list for employee with ID {employee_id}.")
        return
    
    todos = todos_response.json()
    
    # Calculate completed tasks
    completed_tasks = [todo for todo in todos if todo.get("completed")]
    total_tasks = len(todos)
    number_of_done_tasks = len(completed_tasks)
    
    # Display TODO list progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
    
    get_employee_todo_list(employee_id)

