# Input : 153
# Output : Yes
# 153 is an Armstrong number.
# 1*1*1 + 5*5*5 + 3*3*3 =


def is_armstrong(n):
    num = n
    _sum = 0
    while n > 0:
        d = n % 10
        _sum = _sum + (d * d * d)
        n = int(n / 10)
    if _sum == num:
        print("Armstrong Number.")
    else:
        print("Not Armstrong Number.")


is_armstrong(153)
