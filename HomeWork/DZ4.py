number = 56
play = 1

usernumber = int(input('Введите число от 1 до 100, либо 0, чтобы завершить: '))

while usernumber > 0:
    if usernumber > number:
        print('Загаданное число меньше, попробуйте еще раз')
        usernumber = int(input('Введите число между 1 и 100, либо 0, чтобы завершить: '))
        play += 1
    elif usernumber < number:
        print('Загаданное число больше, попробуйте еще раз')
        usernumber = int(input('Введите число между 1 и 100, либо 0, чтобы завершить: '))
        play += 1
    else:
        print('Поздравляю! Вы угадали правильное число! С', play, 'раза')
        break
else:
    print('Игра остановлена')
