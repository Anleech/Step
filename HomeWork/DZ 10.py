print("Даны два словаря: x = {'a': 1, 'b': 2} и y = {'b': 3, 'c': 4}. Объединить их в третий словарь")

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = x.copy()
z.update(y)

print()
print(z)
