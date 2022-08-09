while True:
    print("Выберите операцию:",
          "1 -\"r\" - применяет унарный минус к операнду",
          "2 - \"+\" - сложение",
          "3 - \"-\" - вычитание",
          "4 - \"/\" - деление",
          "5 - \"*\" - умножение",
          "6 - \"%\" - деление по модулю (остаток от деления)",
          "7 - \"<\" - минимальное из двух чисел",
          "8 - \">\" - максимальное из двух чисел",
          "0 - \"STOP\" - остановить работу", sep="\n")
    try:
        operation = input('Введите номер операции: ')
        if operation == '0':
            print('Работа остановлена')
            break
        elif operation == '1':
            number = int(input('Введите число: '))
            result = -number
            print('Результат', result)
        elif operation == ('2' or '3' or '4' or '5' or '6' or '7' or '8'):
            number1 = int(input('Введите первое число: '))
            number2 = int(input('Введите второе число: '))
            if operation == '2':
                result = number1 + number2
                print('Результат: ', number1, '+', number2, '=', result)
            elif operation == '3':
                result = number1 - number2
                print('Результат: ', number2, '-', number1, '=', result)
            elif operation == '4':
                if number2 == 0:
                    print('Деление на ноль не возможно')
                else:
                    result = number1 / number2
                    print('Результат: ', number1, '/', number2, '=', result)
            elif operation == '5':
                result = number1 * number2
                print('Результат: ', number1, '*', number2, '=', result)
            elif operation == '6':
                result = number1 % number2
                print('Остаток от деления', number1, 'на', number2, '=', result)
            elif operation == '7':
                if number1 > number2:
                    print('Минимальным из', number1, 'и', number2, 'является', number2)
                elif number1 < number2:
                    print('Минимальным из', number1, 'и', number2, 'является', number1)
                else:
                    print('Числа', number1, 'и', number2, 'равны')
            elif operation == '8':
                if number1 > number2:
                    print('Максимальным из', number1, 'и', number2, 'является', number1)
                elif number1 < number2:
                    print('Максимальным из', number1, 'и', number2, 'является', number2)
                else:
                    print('Числа', number1, 'и', number2, 'равны')
        else:
            print("Введена не корректная операция")
    except ValueError:
        print('Ошибка ввода данных')
