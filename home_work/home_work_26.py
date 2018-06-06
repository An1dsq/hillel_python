import random


def calc_frequency(lst):  # returns the most frequent number or None
    count_1 = count_2 = count_3 = 0
    result = 0
    for elem in lst:
        if elem == -1:
            count_1 += 1
        elif elem == 0:
            count_2 += 1
        elif elem == 1:
            count_3 += 1
    if count_1 == count_2 or count_1 == count_3 or count_2 == count_3:
        return None
    else:
        if count_1 > count_2 and count_1 > count_3:
            result = -1
        elif count_2 > count_1 and count_2 > count_3:
            result = 0
        elif count_3 > count_1 and count_3 > count_2:
            result = 1
    return result


rand_list = [random.randint(-1, 1) for _ in range(11)]
print(rand_list)
print(calc_frequency(rand_list))
