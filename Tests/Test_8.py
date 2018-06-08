import random


def min_max_switcher(lst):
    biggest = lst.index(max(lst))
    lowest = lst.index(min(lst))
    lst[biggest], lst[lowest] = lst[lowest], lst[biggest]


lst1 = [random.randrange(1, 101, 1) for _ in range (10)]
print(id(lst1), lst1)
min_max_switcher(lst1)
print(id(lst1), lst1)

