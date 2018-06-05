
def group_by_surname(list_of_enrollees):  # returns 4 ints
    a_i_group = j_p_group = q_t_group = u_z_group = 0
    for f_name in list_of_enrollees:
        name_char = (f_name.split()[1])[0]
        if ord(name_char) in range(ord('A'), ord('I') + 1):
            a_i_group += 1
        elif ord(name_char) in range(ord('J'), ord('P') + 1):
            j_p_group += 1
        elif ord(name_char) in range(ord('Q'), ord('T') + 1):
            q_t_group += 1
        elif ord(name_char) in range(ord('U'), ord('Z') + 1):
            u_z_group += 1
    return a_i_group, j_p_group, q_t_group, u_z_group
