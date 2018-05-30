
def sum_symbol_codes(first, last):  # returns int
    j = ord(last) - ord(first)
    result = int(ord(first))
    counter = result
    for _ in range(j):
        result += counter + 1
        counter += 1
    return result
