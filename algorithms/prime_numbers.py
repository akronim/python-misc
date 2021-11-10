

def get_primes(start, end):
    primes = []
    for n in range(start, end + 1):
        if is_prime(n):
            primes.append(n)
    return primes


def is_prime(num):
    # prime numbers are greater than 1
    if num > 1:
        m = num // 2
        for i in range(2, m + 1):
            # If num is divisible by any number between
            # 2 and m + 1, it is not prime
            if (num % i) == 0:
                return False
        return True
    else:
        return False


s = int(input("Start number: "))
e = int(input("End number: "))

result = get_primes(s, e)

for r in result:
    print(r)
