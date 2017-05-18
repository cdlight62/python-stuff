import math

def search_list(a_list, num):
    midpoint = math.ceil(len(a_list)/2)-1
    if num == a_list[midpoint]:
        return True
    elif len(a_list) == 1:
        return False
    elif num < a_list[midpoint]:
        return search_list(a_list[0:midpoint], num)
    elif num > a_list[midpoint]:
        return search_list(a_list[midpoint+1:len(a_list)], num)

a_list = [int(n) for n in input("Enter a list of numbers").split()]
a_list.sort()
num = int(input("Enter a number to search for"))
print(search_list(a_list, num))