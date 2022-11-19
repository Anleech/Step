import json

data = {}


class Encyclopedia:
    def __init__(self, country, capital):
        self.country = country
        self.capital = capital
        # data[self.country] = 'encyclopedia'

    def __str__(self):
        return f'{self.country}: {self.capital}'

    @classmethod
    def set_country(cls, add_country, add_capital):
        try:
            new_data = json.load(open('encyclopedia.json'))
        except FileNotFoundError:
            new_data = {}
        new_data[add_country] = add_capital

        with open('encyclopedia.json', 'w') as f:
            json.dump(new_data, f, indent=2)

    @classmethod
    def dell_country(cls, dell_country):
        try:
            new_data = json.load(open('encyclopedia.json'))
        except FileNotFoundError:
            new_data = {}
        del new_data[dell_country]

        with open('encyclopedia.json', 'w') as f:
            json.dump(new_data, f, indent=2)

    @classmethod
    def search_country(cls, search_country):
        try:
            new_data = json.load((open('encyclopedia.json')))
        except FileNotFoundError:
            new_data = {}

        if search_country in new_data:
            print(f'Страна {search_country} столица {new_data[search_country]}')
        else:
            print(f'Страны {search_country} нет')

    @classmethod
    def edit_country(cls, edit_country, new_capital):
        try:
            new_data = json.load(open('encyclopedia.json'))
        except FileNotFoundError:
            new_data = {}

        new_data[edit_country] = new_capital
        with open('encyclopedia.json', 'w') as f:
            json.dump(new_data, f, indent=3, ensure_ascii=False)

    @classmethod
    def load_file(cls,):
        with open('encyclopedia.json', 'r') as f:
            print(json.load(f))


index = 0
while index != 6:
    try:
        index = int(input('Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n'
                          '4 - редактирование данных\n5 - просмотр данных\n6 - Завершение работы\nВвод: '))
        if index == 1:
            country = input('Введите название страны(с заглавной буквы):')
            capital = input('Введите название столицы страны(с заглавной буквы):')
            Encyclopedia.set_country(country, capital)
            print('Данные записаны')
        if index == 2:
            country = input('Введите страну для удаления(с заглавной буквы):')
            Encyclopedia.dell_country(country)
            print('Данные удалены')
        if index == 3:
            country = input('Введите название страны(с заглавной буквы):')
            Encyclopedia.search_country(country)
        if index == 4:
            country = input('Введите страну для корректировки: ')
            new_capital = input('Введите новое название столицы: ')
            Encyclopedia.edit_country(country, new_capital)
            print('Данные отредактированы')
        if index == 5:
            Encyclopedia.load_file()

    except:
        break
else:
    print('Работа завершена')
