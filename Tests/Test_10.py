sample_lst = [[6, 8, 7],
              [5, 7, 6],
              [2, 9, 7]]

sample_lst2 = [[3, 8, 7, 8],
               [5, 9, 6, 9],
               [2, 6, 7, 6],
               [5, 9, 7, 9]]


def pretty_print(lst):
    for i in range(len(lst)):
        for j in lst[i]:
            print(j, end=' ')
        print()


# def point_seeker(lst):
#     the_point = []
#     for i in range(len(lst)):
#         mi = lst[i].index(max(lst[i]))
#         max_x = min_y = max(lst[i])
#         for j in range(len(lst[i])):
#             tmp_min = int(lst[j][mi])
#             mj = lst.index(lst[i])
#             if tmp_min < min_y:
#                 min_y = lst[j][mi]
#                 mj = j
#         if max_x == min_y:
#             the_point.append(mj)
#             the_point.append(mi)
#     for i in range(len(lst)):
#         mi = lst[i].index(min(lst[i]))
#         min_x = max_y = min(lst[i])
#         for j in range(len(lst[i])):
#             tmp_max = lst[j][mi]
#             mj = lst.index(lst[i])
#             if tmp_max > max_y:
#                 max_y = lst[j][mi]
#                 mj = j
#         if min_x == max_y:
#             the_point.append(mj)
#             the_point.append(mi)
#     return the_point


def point_seeker(lst):
    pretty_print(lst)
    the_point = []
    alt_lst = list(map(list, zip(*lst)))
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            elem = lst[i][j]
            if is_extreme(elem, lst.index(lst[j]), lst[i]) == 'max':
                if is_extreme(elem, lst.index(lst[j]), alt_lst[i]) == 'min':
                    the_point.append([i, lst[i].index(elem)])
            elif is_extreme(elem, lst.index(lst[j]), lst[i]) == 'min':
                if is_extreme(elem, lst.index(lst[j]), alt_lst[i]) == 'max':
                    the_point.append([i, lst[i].index(elem)])
    return the_point


def is_extreme(elem, index, lst):
    if elem == max(lst) or elem == min(lst):
        if 0 < index < lst.index(lst[-1]):
            if lst[index - 1] < elem and lst[index + 1] < elem:
                return 'max'
            elif lst[index - 1] > elem and lst[index + 1] > elem:
                return 'min'
        if index == 0:
            if lst[index + 1] < elem:
                return 'max'
            elif lst[index + 1] > elem:
                return 'min'
        if index == lst.index(lst[-1]):
            if lst[index - 1] < elem:
                return 'max'
            elif lst[index - 1] > elem:
                return 'min'
    return 'mid'


print(point_seeker(sample_lst))


# max_val = max(sample_lst2[2])
# print(max(sample_lst2[2]))
# max_index = [i for i, j in enumerate(sample_lst2[2]) if j == max_val]
# print(max_index)
