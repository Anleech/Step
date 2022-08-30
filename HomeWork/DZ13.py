# Задание 1
print('Создать лямбда-выражение,которое возвращает произведение трех чисел 2, 5, 5 \n')

print((lambda x, y, z: x * y * z)(2, 5, 5))

# Задание 2
print('Отсортировать список объектов по имени студентов и итоговым оценкам в порядке убывания')
print("Тест:\n"
      "[{'name':'Jennifer', 'final':95},\n{'name':'David', 'final':92},\n{'name':'Nikolas', 'final':98}]")

students = [{'name': 'Jennifer', 'final': 95}, {'name': 'David', 'final': 92}, {'name': 'Nikolas', 'final': 98}]
print()
sort_name = sorted(students, key=lambda item: item['name'])
print(sort_name)
sort_mark = sorted(students, key=lambda item: item['final'], reverse=True)
print(sort_mark)

# Задание 3
print('Получить минимальную и максимальную итоговую оценку студентов')
print("Тест:\n"
      "[{'name':'Jennifer', 'final':95},\n{'name':'David', 'final':92},\n{'name':'Nikolas', 'final':98}]")

students = [{'name': 'Jennifer', 'final': 95}, {'name': 'David', 'final': 92}, {'name': 'Nikolas', 'final': 98}]
print()
maxim = max(students, key=lambda item: item['final'])
print(maxim)
minim = min(students, key=lambda item: item['final'])
print(minim)

# Задание 4
print('Дан список чисел. Используя Lambda-выражение, возведите в квадрат и в куб все элементы данного списка.')
print('nums = [3, 5, 7, 3, 9, 5, 7, 2]')
nums = [3, 5, 7, 3, 9, 5, 7, 2]

square = list(map(lambda i: i ** 2, nums))
cube = list(map(lambda i: i ** 3, nums))
print()
print(square)
print(cube)
