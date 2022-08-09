# Задание 1
# print('Выведите элементы списка с четными индексами.')
# print('Введите элементы списка')
#
# a = [input('-> ') for i in range(int(input('n = ')))]
#
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=' ')


# Задание 2
# print('Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.')
# print('Введите элементы списка')
#
# a = [input('-> ') for i in range(int(input('n = ')))]
#
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=' ')


# Задание 3
print('Вывести треугольник из звездочек')

size = 8

for i in range(size):
    for j in range(1, i + 1):
        print('*', end='')
    print()


# Задание 4
# print('Вывести треугольник из звездочек')
# print()
#
# size = 8
#
# for i in range(size):
#     for j in range(size, i, -1):
#         print('*', end='')
#     print()


# Задание 5  НЕ ПОЛУЧИЛОСЬ СДЕЛАТЬ КВАДРАТ ИЗ СИМВОЛОВ
# print('Написать программу, выводящую чередующиеся квадраты символов в шахматном порядке.')
#
# size = int(input('Введите размер поля: '))
# sumbol = int(input('Введите количество символов: '))
#
# for i in range(size):
#     for j in range(sumbol):
#         for k in range(size):
#             for m in range(sumbol):
#                 if (i+k) % 2 == 0:
#                     print('*', end=' ')
#                 else:
#                     print(' ', end=' ')
#         print()
