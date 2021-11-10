names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
numbers = [5, 2, 1, 7, 4]

print(numbers)      # [5, 2, 1, 7, 4]

names.extend(numbers)

print(names)    # ['John', 'Bob', 'Mosh', 'Sarah', 'Mary', 5, 2, 1, 7, 4]

numbers.append(20)
print(numbers)      # [5, 2, 1, 7, 4, 20]

numbers.insert(0, 10)
print(numbers)      # [10, 5, 2, 1, 7, 4, 20]

print(numbers.index(5))      # 1

numbers.pop()
print(numbers)      # [10, 5, 2, 1, 7, 4]

print(50 in numbers)    # False

print(numbers.count(4))     # 1

numbers.sort()
print(numbers)        # [1, 2, 4, 5, 7, 10]

numbers.remove(5)
print(numbers)      # [1, 2, 4, 7, 10]

numbers.reverse()
print(numbers)      # [10, 7, 4, 2, 1]

numbers2 = numbers.copy()
print(numbers2)     # [10, 7, 4, 2, 1]

print(sum(numbers))

numbers.clear()
print(numbers)      # []

############
numbers = [2, 2, 4, 6, 3, 4, 6, 1, 3]
uniques = []
for n in numbers:
    if n not in uniques:
        uniques.append(n)
print(uniques)



