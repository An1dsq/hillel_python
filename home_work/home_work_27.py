import random
import string


def pemrtuate(text):  # returns permuted text
    words = [word for word in text.split()]
    result = []
    skipped_word_len = 3
    for word in words:
        if len(word) > skipped_word_len:
            if word[-1] in string.punctuation:
                after_word = word[-1]
                new_word = str(letters_mixer(word[:-1])) + after_word
                result.append(new_word)
            else:
                result.append(letters_mixer(word))
        else:
            result.append(word)
    return ' '.join(result)


def letters_mixer(word):
    first_char, part_to_mix, last_char = word[0], list(word[1:-1]), word[-1]
    k = 0
    min_allowed_len = 2
    step = 2
    while 1 + k < len(part_to_mix):
        if len(part_to_mix) > min_allowed_len:
            x = part_to_mix[k:k+step]
            random.shuffle(x)
            part_to_mix[k:k+step] = x
        else:
            random.shuffle(part_to_mix)
        k += step
    return first_char + ''.join(part_to_mix) + last_char


text = '''Напишите функцию, которая преобразует переданный ей текст способом, похожим на описанный выше.
 В качестве алгоритма перемешивания букв в слове используйте следующий'''
print(text)
print(pemrtuate(text))
