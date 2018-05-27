
def sum_of_digits(number):  # returns int
    x1 = number % 10
    y1 = number // 10
    x2 = y1 % 10  # без цикла, громоздко
    y2 = y1 // 10
    x3 = y2 % 10
    return x1 + x2 + x3
