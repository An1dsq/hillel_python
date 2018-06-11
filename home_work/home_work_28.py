import string


def encode(str_to_encode):  # returns enсoded string
    table = string.ascii_lowercase + string.digits
    encoded_str = ''
    step = 5
    for i in range(len(str_to_encode)):
        if str_to_encode[i].lower() in table:
            index = table.find(str_to_encode[i].lower())
            if index >= len(table) - step:
                encoded_str += table[(index + step) % len(table)]
            else:
                encoded_str += table[index + step]
        else:
            encoded_str += str_to_encode[i]
    return encoded_str


print(encode('secret'))
print(encode('Office 365'))
