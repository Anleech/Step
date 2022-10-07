class Converting:
    def __init__(self, a=0):
        self.__killograms = a

    @property
    def c__killograms(self):
        return self.__killograms

    @c__killograms.setter
    def c__killograms(self, a):
        if isinstance(a, (int, float)):
            self.__killograms = a
        else:
            print('Данные должны быть числом')

    def convert(self):
        c = self.__killograms * 2.2046
        return c


c1 = Converting(12)
print(c1.c__killograms, "кг => ", end="")
print(f'{c1.convert():.2f} фунтов')

c1.c__killograms = 41
print(c1.c__killograms, "кг => ", end="")
print(f'{c1.convert():.3f} фунтов')
