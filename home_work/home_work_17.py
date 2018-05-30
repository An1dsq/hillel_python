import math


def solve_quadratic_equation(a, b, c):  # returns 2 values: either 2 roots, 1 root and None or 2 Nones
    discriminant = b**2 - (4 * a * c)
    if discriminant > 0:
        root_1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root_2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root_1, root_2
    elif discriminant == 0:
        root_1 = (-b + math.sqrt(discriminant)) / 2 * a
        return root_1, None
    elif discriminant < 0:
        return None, None
