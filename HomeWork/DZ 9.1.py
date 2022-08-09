# Задание 1
# print('Поиск заданного элемента в кортеже')
#
# tpl = tuple(['ab', 'abcd', 'cde', 'abc', 'def'])
#
# print('Исходный кортеж: ', tpl)
#
# s = input('Введите элемент для поиска: ')
#
# if s in tpl:
#     print('Yes')
# else:
#     print('No')

# Задание 2
print('Введите статистику частотности символов в кортеже')

tpl = tuple(input('Введите по порядку,без пробелов элементы кортежа: '))

unicSumbol = set(tpl)

for i in unicSumbol:
    print('Количество ', i, '=', tpl.count(i))





