import math


def get_max_digit(number):  # returns int
    max_int = 0
    number_temp = number
    for _ in range(int(math.log10(number) + 1)):  # так быстрее)
        digit = number_temp % 10
        number_temp //= 10
        if digit > max_int:
            max_int = digit
    return max_int
