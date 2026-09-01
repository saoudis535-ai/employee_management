import json


FILE_NAME = "employees.json"


def load_employees():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_employees(employees):
    with open(FILE_NAME, "w") as file:
        json.dump(employees, file, indent=4) 