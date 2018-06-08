def is_isogram(text):
    lst = list(''.join(text.split(' ')).lower())
    unique = set(lst)
    return len(lst) == len(unique)
