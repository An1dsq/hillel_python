def exotic_sorter(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i]) - 2):
            if i % 2 == 0:
                sort(lst[i], 0)
            else:
                sort(lst[i], 1)
    return lst


def sort(lst, reverse=0):
    for i in range(len(lst) - 1):
        for _ in lst:
            if reverse:
                if lst[i] > lst[i+1]:
                    lst[i],  lst[i+1] = lst[i+1], lst[i]
                    if i + 1 != len(lst) - 1:
                        i += 1
            else:
                if lst[i] < lst[i+1]:
                    lst[i],  lst[i+1] = lst[i+1], lst[i]
                    if i + 1 != len(lst) - 1:
                        i += 1
    return lst


unsorted_list = [[1, 3, 2], [4, 6, 5], [7, 9, 8], [10, 13, 12], [14, 16, 15], [17, 19, 18]]
print(id(unsorted_list), unsorted_list)
exotic_sorter(unsorted_list)
print(id(unsorted_list), unsorted_list)
