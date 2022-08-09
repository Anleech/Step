# Задание 1
#
# a = [1, 2, 3]
# b = [11, 12, 13, 4, 2]
# c = []
# i = 0
# e = []
#
# if len(a) != len(b):    # Условие если длинны списков не равны
#     if len(a) > len(b):     # список a длиннее
#         while i < len(b):
#             d = a[:len(b)]
#             c.append(d[i])
#             c.append(b[i])
#             i += 1
#             e = a[len(b):]
#     else:                  # список b длиннее
#         d = b[:len(a)]
#         c.append(a[i])
#         c.append(d[i])
#         i += 1
#         e = b[len(a):]
#     print(c + e)
#
# else:                       # списки одной длинны
#     while i < len(a):
#         c.append(a[i])
#         c.append(b[i])
#         i += 1
#     print(c)


# Задание 2
a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
b = []
c = []

while len(a):
    b = a.pop(0)
    if b not in a:
        c.append(b)
    else:
        while b in a:
            a.remove(b)
print(*c)
