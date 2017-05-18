a_list = [int(x) for x in input("Enter a list: ").split()]

print([x for x in a_list if x % 2 == 0])
