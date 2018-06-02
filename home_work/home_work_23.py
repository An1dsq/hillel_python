
def chess_reward():  # returns 2 ints (cell number and total number of corns)
    cell_number = 2
    number_of_corns = 2
    while number_of_corns < 1000000:
        number_of_corns *= 2
        cell_number += 1
    return cell_number - 1, number_of_corns - 1
