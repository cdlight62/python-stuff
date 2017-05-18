def reverse_words(a_list):
    return a_list[::-1]


my_list = [x for x in input("Enter a sentence: ").split(" ")]
print(" ".join(reverse_words(my_list)))