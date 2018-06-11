from random import randint
import string


def pass_gen():
    global counter
    counter += 1
    allowed_chars = string.ascii_letters + '_' + string.digits
    new_pass = ''
    for _ in range(8):
        letter = allowed_chars[randint(1, len(allowed_chars) - 1)]
        new_pass += letter
    if any(char.isupper() for char in new_pass) and any(char.islower() for char in new_pass) and any(char.isdigit() for char in new_pass):
        return new_pass
    else:
        return pass_gen()


counter = 0
print(pass_gen(), counter)
