import json

data = {}


class CountryCapital:
    def __init__(self, country, capital):
        self.country = country
        self.capital = capital
        data[self.country] = 'encyclopedia.json'

    def __str__(self):
        return f'{self.country}: {self.capital}'

    @classmethod
    def edit_country(cls, old_value, new_value, filename):
        try:
            data_new = json.load(open(filename))
        except FileNotFoundError:
            data_new = {}

        data_new[old_value] = new_value
        with open(filename, 'w') as f:
            json.dump(data_new, f, indent=3)

    @classmethod
    def search_country(cls, country, filename):
        try:
            data_new = json.load(open(filename))
        except FileNotFoundError:
            data_new = {}

        if country in data_new:
            print(f'Страна {country} столица {data_new[country]}')
        else:
            print(f'Страны {country} нет')

    @classmethod
    def set_country(cls, new_country, new_capital, filename, ):
        try:
            data_new = json.load(open(filename))
        except FileNotFoundError:
            data_new = {}
        data_new[new_country] = new_capital

        with open(filename, 'w') as f:
            json.dump(data_new, f, indent=3)

    @classmethod
    def dell_country(cls, del_country, filename, ):
        try:
            data_new = json.load(open(filename))
        except FileNotFoundError:
            data_new = {}
        del data_new[del_country]

        with open(filename, 'w') as f:
            json.dump(data_new, f, indent=3)

    @classmethod
    def load_file(cls, filename):
        with open(filename, 'r') as f:
            print(json.load(f))


index = 0
while index != 6:
    try:
        index = int(input('Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n'
                          '4 - редактирование данных\n5 - просмотр данных\n6 - Завершение работы\nВвод: '))
        if index == 1:
            country_name = input('Введите название страны(с заглавной буквы):')
            capital_name = input('Введите название столицы страны(с заглавной буквы):')
            CountryCapital.set_country(country_name, capital_name, 'encyclopedia.json')
            print('Файл сохранен')

        if index == 2:
            country_name = input('Введите страну для удаления(с заглавной буквы):')
            CountryCapital.dell_country(country_name, 'encyclopedia.json')
            print('Файл сохранен')

        if index == 3:
            country_name = input('Введите название страны(с заглавной буквы):')
            CountryCapital.search_country(country_name, 'encyclopedia.json')

        if index == 4:
            country_name = input('Введите страну для корректировки: ')
            new_capital = input('Введите новое название столицы: ')
            CountryCapital.edit_country(country_name, new_capital, 'encyclopedia.json')
            print('Файл сохранен')

        if index == 5:
            CountryCapital.load_file('encyclopedia.json')
    except:
        break
else:
    print('Работа завершена')