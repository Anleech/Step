import re

print('Найти адрес электронной почтыю')
s = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"
print(f'Тест:\n{s}')
reg = r"[-\w.]+@[\w.]+"
print(re.findall(reg, s))
