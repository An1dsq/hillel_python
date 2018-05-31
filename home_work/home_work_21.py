import math


def get_max_digit(number):  # returns int
    max_int = 0
    for _ in range(int(math.log10(number) + 1)):  # так быстрее)
        digit = number % 10
        number //= 10
        if digit > max_int:
            max_int = digit
    return max_int
