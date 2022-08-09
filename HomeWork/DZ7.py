import random as r

# Задание 1
# print('Программа которая находит количество отрицательных элементов')
# n = [[r.randint(-20, 10) for m in range(3)] for y in range(4)]
# z = 0
#
# for row in n:
#     for m in row:
#         print(m, end="\t\t")
#         if m < 0:
#             z += 1
#     print()
#
# print('Количество отрицательных элементов: ', z)


# Задание 2
print('Программа которая находит произведение не нулевых элементов')
n = [[r.randint(0, 4) for m in range(3)] for y in range(4)]
z = 1

for row in n:
    for i in row:
        print(i, end="\t\t")
        if i > 0:
            z *= i
    print()

print('Произведение ненулевых элементов : ', z)


# Задание 3
print('Программа которая заменит строки двумерного списка на одномерный')
n = [[r.randint(0, 10) for m in range(6)] for y in range(6)]
b = [r.randint(0, 10) for m in range(6)]


for row in n:
    for m in row:
        print(m, end="\t\t")
    print()
print(b)
print()

for i in range(len(n)):
    for u in range(len(n)):
        if i % 2 == 0:
            n[i] = [*b]

for row in n:
    for m in row:
        print(m, end="\t\t")
    print()
