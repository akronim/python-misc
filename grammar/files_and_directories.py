from pathlib import Path

# Absolute path C:\Program Files\Microsoft ...
# Relative path:

path = Path("ecommerce")
print(path.exists())

# path = Path("emails")
# path.mkdir()
# path.rmdir()

path = Path()
for file in path.glob('*.*'):
    print(file)

for file in path.glob('*.py'):
    print(file)

print("")

# creating file
employee_file = open("employees.txt", "w")

employee_file.write("Jim - Salesman")
employee_file.write("\nDwight - Salesman")
employee_file.write("\nPam - Receptionist")
employee_file.write("\nMichael - Manager")
employee_file.write("\nOscar - Accountant")

employee_file.close()

# opening file
employee_file = open("employees.txt", "r")  # r => read | w => overwrite | a => append | r+ => reading and writing

print(employee_file.readable())     # checking if readable

# print(employee_file.read())     # read all

print(employee_file.readline())     # reading single line

employees = employee_file.readlines()   # returns a list
for emp in employees:
    print(emp)

employee_file.close()  # do not forget to close

# writing to files
employee_file = open("employees.txt", "a")

employee_file.write("\nToby - Human Resources")
employee_file.write("\nKelly - Customer Service")

employee_file.close()

