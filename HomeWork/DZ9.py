def rectangle():
    a = float(input('Введите длину прямоугольника: '))
    b = float(input('Введите ширину прямоугольника: '))
    s = a * b
    return s


def triangle():
    a = float(input('Введите основание треугольника: '))
    b = float(input('Введите высоту треугольника: '))
    s = (a * b) / 2
    return s


def circle():
    r = float(input('Введите радиус круга: '))
    s = 3.14 * (r ** 2)
    return s


print('Напишите функции нахождения площади фигур:', end='\n\n')

figure = input('1-Прямоугольник, 2-Треугольник, 3-Круг: ')
try:
    if figure == '1':
        print(f'Площадь: {rectangle():.2f}')
    elif figure == '2':
        print(f'Площадь: {triangle():.2f}')
    elif figure == '3':
        print(f'Площадь: {circle():.2f}')
    else:
        print('Ошибка.Нет такой фигуры')
except ValueError:
    print('Ошибка ввода данных')
