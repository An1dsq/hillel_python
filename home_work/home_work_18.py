
def sum_symbol_codes(first, last):  # returns int
    j = ord(last) - ord(first)
    distance = ord(first)
    counter = distance
    for _ in range(j):
        distance += counter + 1
        counter += 1
    return distance
