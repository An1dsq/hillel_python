approved_chars = [str(i) for i in range(10)]
number = input('Введи пятизначное число: ')
result = 1
for letter in number:
    if letter in approved_chars:
        digit = int(letter)
        if digit % 2 != 0:
            result *= digit
print('Произведение нечётных цифр:', result)
