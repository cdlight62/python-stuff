import random

def cows_and_bulls(num, guess):
    cows = 0
    bulls = 0
    for i in range(len(num)):
        if num[i] == guess[i]:
            cows +=1
        else:
            bulls += 1
    return [cows, bulls]

if __name__ == "__main__":
    cont = True
    count = 0
    num = [int(n) for n in str(random.randint(1000, 10000))]
    while cont:
        guess = input("Enter a 4 digit number")
        if guess in ["q", "quit", "exit"]:
            break
        else:
            guess = [int(n) for n in guess]
            count += 1
        cowsandbulls = cows_and_bulls(num, guess)
        cows = cowsandbulls[0]
        bulls = cowsandbulls[1]
        print(str(cows) + (" cow, " if cows == 1 else " cows, ") + str(bulls) + (" bull" if bulls == 1 else " bulls"))
        if cows == 4:
            cont = False
    print(str(count) + " guesses")