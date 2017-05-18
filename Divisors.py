num = int(input("Enter a number: "))

for n in range(1, num):
    if num % n == 0:
        print(n)