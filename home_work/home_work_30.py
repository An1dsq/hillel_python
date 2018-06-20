
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def prime_list():
    for num in range(2, 101):
        if is_prime(num):
            print(num)


prime_list()
