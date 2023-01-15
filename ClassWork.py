from jinja2 import Template

# name = "Игорь"
# age = 28
#
# per = {'name': "Игорь", 'age': 28}
#
# tm = Template("Мне {{ p.age }} лет и меня зовут {{ p.name }}")
# msg = tm.render(p=per)
#
# print(msg)

#
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
# per = Person("Игорь", 28)
#
# tm = Template("Мне {{ p.get_age() }} лет и меня зовут {{ p.get_name() }}")
# msg = tm.render(p=per)
#
# print(msg)


# data = """"{% raw %}Модуль Jinja вместо
# определения {{name}}
# подставит соответствующее значение {% endraw %}
# """
#
# tm = Template(data)
# msg = tm.render(name="Игорь")
#
# print(msg)

# link = """
# В HTML-Документе определяется так:
# <a href="#">Ссылка</a>
# """
#
# tm = Template("{{ link | e }}")
# msg = tm.render(link=link)
#
# print(msg)

# cities = [
#     {'id':1, 'city': 'Мосвка'},
#     {'id':2, 'city': 'Сочи'},
#     {'id':3, 'city': 'Смоленск'},
#     {'id':4, 'city': 'Минск'},
#     {'id':5, 'city': 'Ярославль'}
# ]
#
# link = """
# <select name="cities">
# {% for c in cities -%}
#     <option value="{{ c['id'] }}">{{  c['city'] }}</option>
# {% endfor -%}
# </select>
# """
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)


# persons = [
#     {'name':'Алексей', 'year': 18, 'weight': 75},
#     {'name':'Никита', 'year': 28, 'weight': 78.7},
#     {'name':'Виталий', 'year': 35, 'weight': 99},
#     ]
#
# tpl = """
# {%- for u in user -%}
#     {% filter upper %} {{ u.name }} {% endfilter %} {% filter string %} {{ u.year }} - {{ u.weight }} {% endfilter %}
# """
#
# tm = Template(tpl)
# msg = tm.render(user=persons)
#
# print(msg)


html = """

"""

tm = Template(html)
msg = tm.render(user=persons)

print(msg)