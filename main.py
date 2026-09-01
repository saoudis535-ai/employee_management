from employee import Employee
from storage import load_employees, save_employees


employees = load_employees()


def add_employee():

    name = input("Enter employee name: ")
    position = input("Enter position: ")

    try:
        salary = float(input("Enter salary: "))

        if salary < 0:
            raise ValueError("Salary cannot be negative")

    except ValueError:
        print("Invalid salary.")
        return

    employee = Employee(name, position, salary)

    employees.append({
        "name": employee.name,
        "position": employee.position,
        "salary": employee.salary
    })

    save_employees(employees)

    print("Employee added successfully.")


def show_employees():

    if not employees:
        print("No employees found.")
        return

    for employee in employees:
        print(
            f'{employee["name"]} - '
            f'{employee["position"]} - '
            f'{employee["salary"]}'
        )


def search_employee():

    name = input("Enter employee name: ")

    for employee in employees:

        if employee["name"].lower() == name.lower():
            print(
                f'Name: {employee["name"]}\n'
                f'Position: {employee["position"]}\n'
                f'Salary: {employee["salary"]}'
            )
            return

    print("Employee not found.")


def show_high_salary_employees():

    high_salary = [
        employee
        for employee in employees
        if employee["salary"] >= 70000
    ]

    if not high_salary:
        print("No high salary employees.")
        return

    for employee in high_salary:
        print(employee)


def delete_employee():

    name = input("Enter employee name: ")

    for employee in employees:

        if employee["name"].lower() == name.lower():

            employees.remove(employee)
            save_employees(employees)

            print("Employee deleted successfully.")
            return

    print("Employee not found.")
def main():

    while True:

        print("\n===== Employee Management System =====")
        print("1. Add employee")
        print("2. Show employees")
        print("3. Search employee")
        print("4. Show high salary employees")
        print("5. Delete employee")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            show_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            show_high_salary_employees()

        elif choice == "5":
            delete_employee()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()      














