print('''Создать класс Student? который будет содержать имя и распечатывать информацию,а иак же вложенный класс,
который будет содержать информацию о ноутбуке с техническими характеристиками: модель, процессор и память.
''')


class Student:
    def __init__(self, name):
        self.name = name
        self.notebook = self.Notebook()

    class Notebook:
        def model(self):
            return "HP"

        def cpy(self):
            return "i7"

        def ram(self):
            return "16"


s1 = Student('Roman')
my_notebook = s1.notebook
print(f'{s1.name} => {my_notebook.model()}, {my_notebook.cpy()}, {my_notebook.ram()}')
s2 = Student('Vladimir')
my_notebook = s2.notebook
print(f'{s1.name} => {my_notebook.model()}, {my_notebook.cpy()}, {my_notebook.ram()}')
