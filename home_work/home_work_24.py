
def group_by_surname(list_of_enrollees):  # returns 4 ints
    a_i_group = j_p_group = q_t_group = u_z_group = 0
    for f_name in list_of_enrollees:
        name_char = (f_name.split()[1])[0]
        if 'A' <= name_char <='I':
            a_i_group += 1
        elif 'J' <= name_char <='P':
            j_p_group += 1
        elif 'Q' <= name_char <='T':
            q_t_group += 1
        elif 'Q' <= name_char <='Z':
            u_z_group += 1
    return a_i_group, j_p_group, q_t_group, u_z_group
