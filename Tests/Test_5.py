number1, number2 = input('Введи два числа, разделённые пробелом: ').split()
print('Ближайшее к 10:', (number1 if (abs(10 - float(number1)) < (abs(10 - float(number2)))) else number2))
