
def sum_of_fib(count):
    number = 1
    number2 = 1
    result = [number, number2]
    while len(result) < count:
        result.append((number + number2))
        if number < number2:
            number = result[-1]
        else:
            number2 = result[-1]
    print(result)
    return sum(result)


n = 10
print('Сумма первых %d членов последовательности Фибоначчи: %d' % (n, sum_of_fib(n)))
