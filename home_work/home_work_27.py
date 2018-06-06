import random
import string


def pemrtuate(text):  # returns permuted text
    words = [word for word in text.split()]
    result = []
    for word in words:
        if len(word) > 3:
            if word[len(word) - 1] in string.punctuation:
                after_word = word[len(word) - 1]
                new_word = str(letters_mixer(word[:len(word) - 1])) + after_word
                result.append(new_word)
            else:
                result.append(letters_mixer(word))
        else:
            result.append(word)
    return ' '.join(result)


def letters_mixer(word):
    first_char, part_to_mix, last_char = word[0], list(word[1:len(word) - 1]), word[len(word) - 1]
    k = 0
    while 1 + k < len(part_to_mix):
        if len(part_to_mix) > 2:
            x = part_to_mix[k:k + 2]
            random.shuffle(x)
            part_to_mix[k:k+2] = x
        else:
            random.shuffle(part_to_mix)
        k += 2
    return first_char + ''.join(part_to_mix) + last_char


text = '''Напишите функцию, которая преобразует переданный ей текст способом, похожим на описанный выше.
 В качестве алгоритма перемешивания букв в слове используйте следующий'''
print(text)
print(pemrtuate(text))
