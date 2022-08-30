# Задание 1
# print('Дано три словаря: {1:10, 2:20},{3:30, 4:40} и {5:50, 6:60}.Объедините данные словари в один')
#
# d1 = {1: 10, 2:20}
# d2 = {3: 30, 4: 40}
# d3 = {5: 50, 6: 60}
# print()
#
# d1.update(d2)
# d1.update(d3)
# print(d1)

# # Задание 2
# print("Дан словарь {'emp1': {'name': 'Jhon', 'salary': 7500},'emp2': {'name': 'Emma', 'salary': 8000},\n"
#       "'emp3': {'name': 'Brad', 'salary': 6500}}.Измените значение зарплаты Бреда с 6500 на 8500")
#
# d = {'emp1': {'name': 'Jhon', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000},
#      'emp3': {'name': 'Brad', 'salary': 6500}}
#
# print()
#
# print(d['emp3'])
# d['emp3']['salary'] = 8500
#
# for i in d:
#     print(i)
#     for x in d[i]:
#         print(x, ":", d[i][x])

# Задание 3
print('пользователь вводит данные о количестве студентов, их фамилии, имена и балл для каждого.\n'
      'Программа должна определить средний балл и вывести фамилии и имена студентов, чей балл выше среднего')
print()

students = {}
student_value = int(input('Количество студентов: '))
marks = 0
for i in range(student_value):
    number = input(str(i+1) + '-й студент: ')
    mark = int(input('Балл: '))
    students[number] = mark
    marks += mark

average = marks / student_value
print()
print(f'Средний балл: {average:.0f}. Студенты с баллом выше среднего:')
for i in students:
    if students[i] > average:
        print(i)