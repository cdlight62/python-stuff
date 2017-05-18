import time

name = input("What is your name?")
age = int(input("How old are you?"))
copies = int(input("How many copies?"))
years_until_100 = 100 - age
date = int(time.strftime("%Y")) + years_until_100
for i in range(0, copies):
    print("Hello " + name + ", you will turn 100 in " + str(date) + "\n")