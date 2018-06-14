def exotic_sorter(lst):
    mix_lst = list(map(list, zip(*lst)))
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if i % 2 == 0:
                mix_lst[i].sort(reverse=True)
            else:
                mix_lst[i].sort()
    result = list(map(list, zip(*mix_lst)))
    return result


def pretty_print(lst):
    for i in range(len(lst)):
        for j in lst[i]:
            print(j, end=' ')
        print()


unsorted_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
pretty_print(unsorted_list)
print('----------')
pretty_print(exotic_sorter(unsorted_list))

