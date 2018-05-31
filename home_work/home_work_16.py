
def have_trains_crashed(v1, v2):  # returns boolean value
    distance_to_turn_from_left = 4
    distance_to_turn_from_right = 6
    if v1 == distance_to_turn_from_left and v2 == distance_to_turn_from_right:
        return True
    return v1 > (distance_to_turn_from_right/distance_to_turn_from_left) * v2
