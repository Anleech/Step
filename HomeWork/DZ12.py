import math

print(
    'Написать функцию, принимающую некоторую информацию о геометрической фигуре и рассчитывающую площадь данной фигуры')
print()
print("Тестовые значения:figure_type = 'rhombus', d1=10, d2=8 \nfigure_type='square', c=5"
      "\nfigure_type='trapezoid', a=12, b=3, h=6 \nfigure_type='circle', r=18 \nfigure_type='unknown', a=1, b=2, c=3")


def figure_area(figure_type=None, **kwargs):
    if figure_type == 'rhombus':
        d1 = kwargs.get('d1')
        d2 = kwargs.get('d2')
        s = (d1 * d2) / 2
        return s
    elif figure_type == 'square':
        c = kwargs.get('c')
        s = c ** 2
        return s
    elif figure_type == 'trapezoid':
        a = kwargs.get('a')
        b = kwargs.get('b')
        h = kwargs.get('h')
        s = (0.5 * ((a + b) * h))
        return s
    elif figure_type == 'circle':
        r = kwargs.get('r')
        p = math.pi
        s = p * (r ** 2)
        return s
    else:
        return 'invalid data'


print()
print(figure_area(figure_type='rhombus', d1=10, d2=8))
print(figure_area(figure_type='square', c=5))
print(figure_area(figure_type='trapezoid', a=12, b=3, h=6))
print(figure_area(figure_type='circle', r=18))
print(figure_area(figure_type='unknown', a=1, b=2, c=3))
