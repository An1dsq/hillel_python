import math


def cone_square_and_volume(radius, height): # returns 2 floats
    hypotenuse = math.sqrt(radius**2 + height**2)
    cone_square = math.pi * radius**2 + math.pi * radius * hypotenuse
    cone_volume = (math.pi * radius**2 * height)/3
    return cone_square, cone_volume
