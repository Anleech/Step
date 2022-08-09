# Задание 1
# a = 5
# b = 8
# print("a =", a, "b=", b)
#
# a = a + b  # 5+8=13; a=13;b=8
# b = a - b  # 13-8=5: a=13;b=5
# a = a - b  # 13-5=8: a=8;b=5
# print("a =", a, "b=", b)

# Задание 2
# print('Введите последовательно четыре числа')
# number1 = int(input('Введите первое чило: '))
# number2 = int(input('Введите второе чило: '))
# number3 = int(input('Введите третье чило: '))
# number4 = int(input('Введите четвертое чило: '))
#
# result = (number1 + number2) / (number3 + number4)
#
# print('Результат :', format(result, '.2f'))

# Задание 3
number = int(input('Введите пятизначное число: '))  # 12345

number1 = number % 10  # 5
number2 = (number // 10) % 10  # 4
number3 = (number // 100) % 10  # 3
number4 = (number // 1000) % 10  # 2
number5 = (number // 10000) % 10  # 1

productnumbers = number1 * number2 * number3 * number4 * number5

arithmeticalmean = (number1 + number2 + number3 + number4 + number5) / 5

print('Произведение цифр числа', number, ':', productnumbers)
print('Среднее арифметическое:', arithmeticalmean)
