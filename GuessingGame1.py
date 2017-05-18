import random

rand = random.randint(1, 99)
num = 0
guesses = 0
guessed = True
while num != rand:
    guesses += 1
    num = input("Guess a number between 1 and 9: ")
    if num in ["q", "quit", "exit"]:
        guessed = False
        break
    else:
        num = int(num)
    if num < rand:
        print("Too low")
    elif num > rand:
        print("Too high")

if guessed:
    print("You got it in " + str(guesses) + " guesses")

