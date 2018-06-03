SPECIAL_COLOUR = '\033[93m'
REGULAR_COLOUR = '\033[0m'


def print_mult_table(n, m):  # prints multiplication table n x m
    for i in range(n + 1):
        for j in range(m + 1):
            pretty_coef = '%' + str(len(str(n * m)) + 1) + 'd'
            if i == 0:
                i = 1
                first_row = SPECIAL_COLOUR + pretty_coef % j
                print(first_row, end='')
            else:
                if j == 0:
                    first_column = SPECIAL_COLOUR + pretty_coef % i + REGULAR_COLOUR
                    print(first_column, end='')
                else:
                    print(pretty_coef % (i * j), end='')
        print()
