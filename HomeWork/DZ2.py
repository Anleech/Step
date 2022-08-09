kopeeiki = int(input('Введите поличество копеек: '))

if 1 <= kopeeiki <= 99:
    if kopeeiki == 1 or (20 < kopeeiki and (kopeeiki % 10) == 1):
        print(kopeeiki, 'копейка')
    elif (2 <= kopeeiki <= 4 or 2 <= (kopeeiki % 10) <= 4) and 15 < kopeeiki < 20:
        print(kopeeiki, 'копейки')
    else:
        print(kopeeiki, 'копеек')
else:
    print('Ошибка')
