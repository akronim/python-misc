names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']

print(names)

print(names[0])

print(names[-1])    # Mary

print(names[2:])    # ['Mosh', 'Sarah', 'Mary']

print(names[2:4])   # ['Mosh', 'Sarah']

print(names[:4])    # ['John', 'Bob', 'Mosh', 'Sarah']

print(names[:])     # ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']

names[0] = 'Tom'
print(names)        # ['Tom', 'Bob', 'Mosh', 'Sarah', 'Mary']

###############

numbers = [3, 6, 2, 8, 4, 10]
_max = numbers[0]
for n in numbers:
    if n > _max:
        _max = n
print(_max)
