birth_year = input("Birth year: ")
print(type(birth_year))

age = 2020 - int(birth_year)        # float(), bool()...
print(age)

print(type("abc"))                  # <class 'str'>
print(type(123))                    # <class 'int'>

weight_kg = input("Weight (kg): ")
weight_lbs = int(weight_kg) / 0.45
print(weight_lbs)

my_num = 5
print(str(my_num))
