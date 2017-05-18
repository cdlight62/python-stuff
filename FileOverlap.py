with open('Primes.txt', 'r') as primes_file, open('Happy_Numbers.txt', 'r') as happy_file:
    matches = []
    primes = [x.strip() for x in primes_file.readlines()]
    happy = happy_file.readline().strip()
    while happy:
        if happy in primes:
            matches.append(happy)
        happy = happy_file.readline().strip()
print(matches)