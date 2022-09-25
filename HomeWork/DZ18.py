# Задание 1
# print('''Обмен местами двух строк в файле
# Тест:
# Замена строки в текстовом файле
# изменить строку в списке
# записать список в файл
# ''')
#
# f = open("text.txt", "w")
# f.write("Замена строки в текстовом документе;\nизменение строки в списке;\nзаписать список в файл;\n")
# f.close()
#
# f = open("text.txt", "r")
# read_f = [li for li in f.readlines()]
# pos1 = int(input('pos1 = '))
# pos2 = int(input('pos2 = '))
# if 0 <= pos1 <= len(read_f) and 0 <= pos2 <= len(read_f) and pos1 != pos2:
#     read_f[pos1], read_f[pos2] = read_f[pos2], read_f[pos1]
# else:
#     print("Индекс введен неверно!")
# f.close()
#
# f = open("text.txt", "w")
# for i in read_f:
#     f.write(i)
# f.close()
#
# f = open("text.txt", "r")
# for i in f:
#     print(i, end='')
# f.close()

# Задание 2
# print('''Реверсирование строк файла (перестановка строк в обратном порядке)
# Тест:
# Замена строки в текстовом файле
# изменить строку в списке
# записать список в файл
# ''')
#
# f = open("text.txt", "w")
# f.write("Замена строки в текстовом документе;\nизменение строки в списке;\nзаписать список в файл;\n")
# f.close()
#
# f = open("text.txt", "r")
# read_f = [li for li in f.readlines()]
# read_f.reverse()
# f.close()
#
# f = open("text.txt", "w")
# for i in read_f:
#     f.write(i)
# f.close()
#
# f = open("text.txt", "r")
# read_file = [li for li in f.readlines()]
# for i in read_file:
#     print(i, end='')
# f.close()

# Задание 3

print('Объединение двух файлов')

f1 = open("text1.txt", "w")
f1.write("Тааль.\nПресноводное озеро Филиппин.\nНаходится на острове Лусон.\nВ провинции Батангас.\n")
f1.close()
f2 = open("text2.txt", "w")
f2.write("Озеро заполняет большую вулканическую кальдеру Тааль.\nОобразованную очень большим извержением.\n")
f2.close()

f1 = open("text1.txt", "r")
read_f1 = [li for li in f1.readlines()]
f1.close()
f2 = open("text2.txt", "r")
read_f2 = [li for li in f2.readlines()]
f2.close()

file3 = read_f1+read_f2

f3 = open("text3.txt", "w")
for i in file3:
    f3.write(i)
f3.close()

