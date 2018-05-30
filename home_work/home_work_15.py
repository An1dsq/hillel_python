import math


def circles_intersect_using_vectors(x1, y1, r1, x2, y2, r2):  # returns boolean value
    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    sum_of_r = r1 + r2
    diff_of_r = abs(r1 - r2)
    if distance == 0 and diff_of_r == 0:  # common center, intersect (infinite number of common points)
        return True
    elif x1 == x2 and y1 == y2 and r1 != r2:  # common center, not intersect
        return False
    elif distance == diff_of_r:  # smaller inside bigger, intersect (1 common point)
        return True
    elif distance < diff_of_r:  # smaller inside bigger, not intersect
        return False
    elif distance < sum_of_r:  # circles not too far (2 common points)
        return True
    elif distance > sum_of_r:  # circles too far
        return False
    elif distance == sum_of_r:  # circles just far enough (1 common point)
        return True
