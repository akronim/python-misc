def print_fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        last1 = fib[-1]
        last2 = fib[-2]
        fib.append(last1 + last2)
    return fib


res = print_fibonacci(9)
print(res)


def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(9))
