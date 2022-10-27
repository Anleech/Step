import math

print("""Создать класс Shape и три дочерних класса: Square, Rectangle, Triangle.
Родительский класс должен иметь абстрактные методы нахождения периметра, площади, рисования фигуры и вывода информации.
С помощью полиморфизма реализуйте вывод информации о дочерних фигурах.
""")


class Shape:
    def __init__(self, color):
        self.color = color

    def perimeter(self):
        raise NotImplementedError("В дочернем классе должен быть определен метод perimeter()")

    def area(self):
        raise NotImplementedError("В дочернем классе должен быть определен метод area()")

    def fig_info(self):
        raise NotImplementedError("В дочернем классе должен быть определен метод fig_info()")

    def draw(self):
        raise NotImplementedError("В дочернем классе должен быть определен метод draw()")


class Square(Shape):
    def __init__(self, color, a):
        super().__init__(color)
        self.sidea = a

    def perimeter(self):
        perimeter = self.sidea * 4
        return perimeter

    def area(self):
        return self.sidea**2

    def draw(self):
        for i in range(self.sidea):
            for j in range(self.sidea):
                print('*', end='')
            print()

    def fig_info(self):
        print(f'===Квадрат===\nСторона: {self.sidea}\nЦвет: {self.color}\nПлощадь: {self.area()}\n'
              f'Периметр: {self.perimeter()}')


class Rectangle(Shape):
    def __init__(self, color, a, b):
        super().__init__(color)
        self.sidea = a
        self.sideb = b

    def perimeter(self):
        perimeter = self.sidea * 2 + self.sideb * 2
        return perimeter

    def area(self):
        area = self.sidea * self.sideb
        return area

    def draw(self):
        for i in range(self.sidea):
            for j in range(self.sideb):
                print('*', end='')
            print()

    def fig_info(self):
        print(f'\n\n===Прямоугольник===\nДлинна: {self.sidea}\nШирина: {self.sideb}\nЦвет: {self.color}\nПлощадь: {self.area()}'
              f'\nПериметр: {self.perimeter()}')


class Triangle(Shape):
    def __init__(self, color, a, b, c,):
        super().__init__(color)
        self.sidea = a
        self.sideb = b
        self.sidec = c

    def perimeter(self):
        perimeter = self.sidea + self.sideb + self.sidec
        return perimeter

    def area(self):
        half_perimeter = self.perimeter()/2
        area = half_perimeter*((half_perimeter-self.sidea)*(half_perimeter-self.sideb)*(half_perimeter-self.sidec))
        sqrt = math.sqrt(area)
        return sqrt

    def draw(self):
        s = self.sideb - 1
        i = 1
        while s > -1:
            print(' ' * s + '*' * i)
            i += 2
            s -= 1

    def fig_info(self):
        print(f'\n\n===Треугольник===\nСторона 1: {self.sidea}\nСторона 2: {self.sideb}\nСторона 3: {self.sidec}'
              f'\nЦвет: {self.color}\nПлощадь: {self.area():.2f}\nПериметр: {self.perimeter()}')


fig1 = Square('red', 3)
fig2 = Rectangle('green', 3, 7)
fig3 = Triangle('yellow', 11, 6, 6)
array = [fig1, fig2, fig3]
for f in array:
    f.fig_info()
    f.draw()
