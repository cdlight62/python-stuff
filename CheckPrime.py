def get_divisors(num):
    return [n for n in range(2, num - 1) if num % n == 0]

num = get_divisors(int(input("Enter a number: ")))
print("prime" if not num else "not prime")