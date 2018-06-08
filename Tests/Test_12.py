from random import randint
already_printed = {0}
result = 0
while result < 15:
    x = randint(2, 9)
    y = randint(2, 9)
    ident = str(x) + str(y)
    ident2 = str(y) + str(x)
    if ident not in already_printed or ident2 not in already_printed:
        print(x, ' x ', y)
        already_printed.add(ident)
        already_printed.add(ident2)
        result += 1
