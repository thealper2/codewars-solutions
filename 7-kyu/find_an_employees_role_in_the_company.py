def find_employees_role(name):
    for employee in employees:
        employee_name = f"{employee['first_name']} {employee['last_name']}"
        if employee_name == name:
            return employee["role"]

    return "Does not work here!"
