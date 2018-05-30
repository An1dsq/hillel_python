import random


def diff_min_max(num_limit, lower_bound, upper_bound):  # returns int
    box = []
    for i in range(num_limit):
        r_range = random.randint(lower_bound, upper_bound)
        box.append(r_range)
    return max(box) - min(box)
