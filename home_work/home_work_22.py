import random
import time
number = random.randint(1, 10)
attempt = 0
when_things_went_wrong = time.time()
approved_chars = [str(i) for i in range(1, 11)]
while True:
    if attempt == 0:
        ges = input('Угадай число от 1 до 10: ')
    elif attempt == 1:
        print('Да ладно, с кем не бывает')
        ges = input('Попробуй ещё разок: ')
    else:
        msg = 'Это ж надо, уже %s раз%s не повезло' % (attempt, '' if attempt in range(5, 22) else 'a')
        print(msg)
        ges = input('Попробуй ещё разок: ')
    attempt += 1
    if ges in approved_chars:
        ges = int(ges)
        if ges < number:
            print('Маловато')
        elif ges > number:
            print('Не, ну это уже перебор')
        elif ges == number:
            print('Ну наконец')
            waste_time = time.time() - when_things_went_wrong
            print('Поздравляю, ты постарел на ' + str(int(waste_time)) + ' сек')
            break
    else:
        print('Так низя')
