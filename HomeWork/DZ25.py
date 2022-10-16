print('''Создать класс Student? который будет содержать имя и распечатывать информацию,а иак же вложенный класс,
который будет содержать информацию о ноутбуке с техническими характеристиками: модель, процессор и память.
''')


class Student:
    def __init__(self, name):
        self.name = name
        self.notebook = self.Notebook()

    def show(self):
        print(self.name, end='')
        self.notebook.show()

    class Notebook:
        def __init__(self):
            self.model = "HP"
            self.ram = "i7"
            self.cpy = "16"

        def show(self):
            print(f' => {self.model}, {self.cpy}, {self.ram}')


s1 = Student('Roman')
s2 = Student('Vladimir')

s1.show()
s2.show()
