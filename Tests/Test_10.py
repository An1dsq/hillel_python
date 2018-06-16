sample_lst = [[6, 8, 7],
              [5, 7, 6],
              [2, 9, 7]]

sample_lst2 = [[3, 8, 7, 8],
               [5, 9, 6, 9],
               [2, 8, 7, 6],
               [5, 9, 7, 9]]


def pretty_print(lst):
    for i in range(len(lst)):
        for j in lst[i]:
            print(j, end=' ')
        print()


def point_seeker(lst):
    pretty_print(lst)
    the_points = []
    alt_lst = list(map(list, zip(*lst)))
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            elem = lst[i][j]
            if how_much_extreme(elem, j, lst[i]) == 'max':
                if how_much_extreme(elem, i, alt_lst[j]) == 'min':
                    the_points.append([i, j])
            elif how_much_extreme(elem, j, lst[i]) == 'min':
                if how_much_extreme(elem, i, alt_lst[j]) == 'max':
                    the_points.append([i, j])
    return the_points


def how_much_extreme(elem, index, lst):
    if elem == max(lst) or elem == min(lst):
        if 0 < index < len(lst) - 1:
            if lst[index - 1] < elem and lst[index + 1] < elem:
                return 'max'
            elif lst[index - 1] > elem and lst[index + 1] > elem:
                return 'min'
        if index == 0:
            if lst[index + 1] < elem:
                return 'max'
            elif lst[index + 1] > elem:
                return 'min'
        if index == len(lst) - 1:
            if lst[index - 1] < elem:
                return 'max'
            elif lst[index - 1] > elem:
                return 'min'
    return 'mid'


print(point_seeker(sample_lst2))
