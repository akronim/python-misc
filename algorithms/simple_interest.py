# Simple interest formula is given by:
# Simple Interest = (P x T x R)/100
# Where,
# P is the principle amount
# T is the time and
# R is the rate

# Input : P = 10000
#         R = 5
#         T = 5
# Output :2500
# We need to find simple interest on
# Rs. 10,000 at the rate of 5% for 5
# units of time.


def simple_interest(p, t, r):
    return (p * t * r) / 100


result = simple_interest(10000, 5, 5)

print(f'The Simple Interest is {result}')
