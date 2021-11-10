try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError as err:
    print('Age cannot be 0.')
    print(err)
except ValueError:
    print("Invalid value")
