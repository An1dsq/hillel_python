import random


def shuffle_list(lst): # no return (shuffles list in place)
    for i in range(len(lst) - 1):
        j = random.randint(0, len(lst) - 1)
        lst[i], lst[j] = lst[j], lst[i]


# list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(id(list1))
# print(list1)
# shuffle_list(list1)
# print(list1)
# print(id(list1))
