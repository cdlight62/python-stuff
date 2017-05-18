def answer1(l):
    import itertools
    l = sorted(l, reverse=True)
    digit = len(l)
    swap = 1
    for i in range(len(l)):
        for p in itertools.permutations(l, len(l)-i):
            signal = int(''.join(map(str, p)))
            if int(''.join(map(str, p)))%3 == 0:
                return signal
    return 0


def answer(l):
    import itertools
    l = sorted(l, reverse=True)
    for i in range(len(l)):
        for p in itertools.combinations(l, len(l)-i):
            signal = int(''.join(map(str, p)))
            if signal%3 == 0:
                return signal
    return 0

print(answer([3, 1, 4, 1, 5]))