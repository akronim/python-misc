# Python3 Program to
# find sum of square
# of first n natural
# numbers

# Input : N = 4
# Output : 30
# 1^2 + 2^2 + 3^2 + 4^2
# = 1 + 4 + 9 + 16
# = 30


def square_sum(n):
    _sum = 0
    for i in range(1, n + 1):
        _sum = _sum + (i * i)

    return _sum


num = 4
print(square_sum(num))
