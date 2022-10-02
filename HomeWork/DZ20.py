import math as mt


class Rectangle:
    def __init__(self, long=0, width=0):
        self.__long = self.__width = 0
        self.__long = long
        self.__width = width

    def __check_value_str(s):
        if not isinstance(s, int):
            print('Данные должны быть числом')
            return False
        return True

    def set_long(self, long):
        if Rectangle.__check_value_str(long):
            self.__long = long

    def set_width(self, width):
        if Rectangle.__check_value_str(width):
            self.__width = width

    def info(self):
        print(f'Длинна прямоугольника: {self.__long}')
        print(f'Ширина прямоугольника: {self.__width}')

    def rect_area(self):
        area = self.__long * self.__width
        print('Площадь прямоугольника: ', area)

    def rect_perimeter(self):
        perimeter = 2 * (self.__long + self.__width)
        print('Площадь прямоугольника: ', perimeter)

    def rect_hypotenuse(self):
        hypotenuse = mt.sqrt(self.__long ** 2 + self.__width ** 2)
        print(f'Гипотенуза прямоугольника: {hypotenuse:.2f}')

    def drawing(self):
        for i in range(self.__long):
            for j in range(self.__width):
                print('*', end='')
            print(end='\n')


r = Rectangle(5, 3)
r.set_long(3)
r.set_width(9)
r.info()
r.rect_area()
r.rect_perimeter()
r.rect_hypotenuse()
r.drawing()
