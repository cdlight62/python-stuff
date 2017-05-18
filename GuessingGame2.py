import math

def midpoint(min, max):
    return math.ceil((min + max)/2)

count = 0
cont = True
min = 0
max = 100
while cont:
    print(midpoint(min, max))
    answer = input()
    if answer == "h":
        max = midpoint(min, max)
    elif answer == "l":
        min = midpoint(min, max)
    elif answer == "c":
        cont = False
    count += 1
print(str(count) + " guesses")