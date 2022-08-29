import random

lst = [random.randint(1, 40) for i in range(10)]


print(lst)
print(list(filter(lambda b: 10 < b < 20, lst)))
