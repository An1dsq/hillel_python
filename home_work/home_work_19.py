import random


def diff_min_max(num_limit, lower_bound, upper_bound):  # returns int
    diff = []
    for i in range(num_limit):
        r_range = random.randint(lower_bound, upper_bound)
        diff.append(r_range)
    return max(diff) - min(diff)
