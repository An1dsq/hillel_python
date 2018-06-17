
def list_archiver(lst, lower_bound, upper_bound):

    old_len = abs(lower_bound) + abs(upper_bound)
    new_len = abs(min(lst)) + abs(max(lst))
    coef = round(old_len / new_len, 1)
    result = []
    for elem in lst:
        new_value = elem * coef
        result.append(round(new_value, 2))
    return result


lst = [-5, 3, 4]
print(list_archiver(lst, -1, 1))
