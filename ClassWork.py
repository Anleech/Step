# x = 0  # Определить переменную цикла
a = 11
b = 6
# for i in range(b):
#     for j in range(0, a - i):
#         print(end=" ")
#     for k in range(a - i, a+1):
#         print("*", end="0")
#
#     print()


# x=6
# for i in range(x):
#     print('%s%s' % ('=' * (x-i-1), '*' * (i*2+1)))

space = b - 1
sign = 1
while space > -1:
    print(' ' * space + '*' * sign)
    sign += 2
    space -= 1
