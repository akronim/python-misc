# Simple Python program to find sum of series
# with cubes of first n natural numbers


# Returns the sum of series
def sum_of_cubes(n):
    _sum = 0
    for i in range(1, n + 1):
        _sum += i * i * i
    return _sum


n = 5
print(sum_of_cubes(n))


