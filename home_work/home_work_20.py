import random


def diff_even_odd(num_limit, lower_bound, upper_bound):  # returns int
    even = []
    odd = []
    for i in range(num_limit):
        r_range = random.randint(lower_bound, upper_bound)
        if r_range % 2 == 0:
            even.append(r_range)
        else:
            odd.append(r_range)
    return sum(even) - sum(odd)
