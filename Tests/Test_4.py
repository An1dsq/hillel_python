number = input('Введи пятизначное число: ')
result = 1
odd_count = 0
for letter in number:
    if letter.isnumeric():
        digit = int(letter)
        if digit % 2 != 0:
            result *= digit
            odd_count += 1
if odd_count == 0:
    print('Барабанил барабанил, а по нечётным так и не попал')
else:
    print('Произведение нечётных цифр:', result)
