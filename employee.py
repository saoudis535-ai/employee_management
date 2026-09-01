class Employee:

    def __init__(self, name: str, position: str, salary: float):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        return f"{self.name} - {self.position} - {self.salary}"

    def is_high_salary(self):
        return self.salary >= 70000 