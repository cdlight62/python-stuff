def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

num = int(input("Number of Fibonacci numbers to generate?"))

print([fibonacci(x) for x in range(1, num + 1)])