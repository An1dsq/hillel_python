
def snake_to_camel(text):
    lst_var_name = text.split('_')
    var_camel_name = ''

    for part_name in lst_var_name:
        var_camel_name += part_name.capitalize()

    return var_camel_name
