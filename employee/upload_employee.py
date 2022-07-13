import csv

from employee import Employee
from redis_om import Migrator

with open("employee.csv") as csv_file:
    employees = csv.DictReader(csv_file)

    for employee in employees:
        emp = Employee(**employee)
        print(f"{employee['firstname']} has pk = {emp.pk}")
        emp.save()

Migrator().run()
