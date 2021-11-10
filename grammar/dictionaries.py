customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer)

print(customer["name"])         # John Smith

print(customer.get("Name"))     # None

customer["name"] = "Jack Smith"
print(customer)         # {'name': 'Jack Smith', 'age': 30, 'is_verified': True}

customer["birthday"] = "Jan 1 1980"
print(customer)     # {'name': 'Jack Smith', 'age': 30, 'is_verified': True, 'birthday': 'Jan 1 1980'}

###########

phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "???") + " "
print(output)

###########

month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(month_conversions["Nov"])
print(month_conversions.get("Nov"))
print(month_conversions.get("Luv"))
print(month_conversions.get("Luv", "Not a valid Key"))
