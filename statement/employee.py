class Employee:
    def __init__(self, code, name):
        self.__code = code
        self.__name = name

    def show_info(self):
        print(f'Заработная плата: {self.__code} - {self.__name}')
