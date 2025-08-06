from add_employee import add_employee
from remove_employee import remove_employee
from search_employee import search_employee

add_employees = []

employees = add_employee(add_employees, "Alice")
employees = add_employee(employees, "Bob")
employees = remove_employee(employees, "Alice")

print(search_employee(employees, "Bob"))  # Should print False
print(search_employee(employees, "Alice"))