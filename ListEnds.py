def get_ends(a_list):
    return [a_list[0], a_list[len(a_list)-1]]

a_list = [int(x) for x in input("Enter a list of numbers: ").split()]
print(get_ends(a_list))