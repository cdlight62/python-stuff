def remove_duplicates(a_list):
    new_list = []
    for x in a_list:
        if not new_list.__contains__(x):
            new_list.append(x)
    return new_list

my_list = [int(x) for x in input("Enter a list of numbers: ").split()]
print(remove_duplicates(my_list))