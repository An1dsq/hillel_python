
def print_mult_table(n, m):  # prints multiplication table n x m
    # matrix = (list(range(1, n + 1)), list(range(1, m + 1)))
    for i in range(n + 1):
        for j in range(m + 1):
            pretty_coef = '%' + str(len(str(n * m)) + 1) + 'd'
            if i == 0:
                i = 1
                first_row = '\033[93m' + pretty_coef % j
                print(first_row, end='')
            else:
                if j == 0:
                    first_column = '\033[93m' + pretty_coef % i + '\033[0m'
                    print(first_column, end='')
                else:
                    print(pretty_coef % (i * j), end='')
        print()


print_mult_table(50, 50)
