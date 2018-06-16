
def list_archiver(lst, lower_bound, upper_bound):
    result = []
    for elem in lst:
        new_value = ((elem - min(lst)) / (max(lst) - min(lst))) * (upper_bound - lower_bound) + lower_bound
        result.append(round(new_value, 2))
    return result


lst = [-5, 3, 4]
print(list_archiver(lst, -1, 1))
