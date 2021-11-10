
for item in 'Python':
    print(item, end=" ")
# P y t h o n

print("")

for item in ["John", "Sarah", "Tom"]:
    print(item, end=" ")
# John Sarah Tom

print("")

friends = ["Jim", "Karen", "Kevin"]

for index in range(len(friends)):
    print(friends[index])

print("")

for item in [1, 2, 3]:
    print(item, end=" ")
# 1 2 3

print("")

for item in range(10):
    print(item, end=" ")
# 0 1 2 3 4 5 6 7 8 9

print("")

for item in range(5, 10):
    print(item, end=" ")
# 5 6 7 8 9

print("")

for item in range(5, 10, 2):    # 2 >>> step
    print(item, end=" ")
# 5 7 9

print("")

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")
