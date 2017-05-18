num = int(input("Enter a number to check: "))
check = int(input("Enter a number to divide by: "))
if(num % check == 0):
    print(str(num) + " divisible by " + str(check))
elif(num % 4 == 0):
    print("divisible by 4")
elif (num % 2 == 0):
    print("even")
else:
    print("odd")