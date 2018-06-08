
def sum_of_fib(count):
    number = 1
    number2 = 1
    result = []  # Don't know how to assign the variables to the list during it's initialization
    result.append(number)
    result.append(number2)
    while len(result) < count:
        result.append((number + number2))
        if number < number2:
            number = int(result[-1])
        else:
            number2 = int(result[-1])
    print(result)
    return sum(result)


n = 10
print('Сумма первых %d членов последовательности Фибоначчи: %d' % (n, sum_of_fib(n)))
