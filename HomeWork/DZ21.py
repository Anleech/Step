class Converting:
    def __init__(self, a=0):
        self.__kilograms = 0
        self.__kilograms = a

    def __check_kilograms_int_float(s):
        if not isinstance(s, int):
            print('Данные должны быть числом')
            return False
        return True

    def set_kilograms(self, a):
        if Converting.__check_kilograms_int_float(a):
            self.__kilograms = a

    def convert(self):
        c = self.__kilograms * 2.2046
        print(f'{self.__kilograms} кг => {c:.3f} фунтов')


# print(Converting.convert(12))

c1 = Converting(12)
c1.convert()
c2 = Converting()
c2.set_kilograms(41)
c2.convert()


