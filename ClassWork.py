import re

s = "Я ищу совпадения в 2021 года. И я из найду в 2 счёта"
reg = r'([0-9]+)\s(\D+)'
print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[0])
# print(m[1])
# print(m[2])
# print(re.findall(reg, s))
print(re.search(reg, s).group(1))
print(re.search(reg, s).group(2))