goods = {
    '1': ['Core-i3-4330', 9, 4500],
    '2': ['Core i5-4670K', 3, 8500],
    '3': ['AMD FX-6300', 6, 3700],
    '4': ['Pentium G3220', 8, 2100],
    '5': ['Core i5-3450', 5, 6400],
}

for key in goods:
    print(key, ') ', goods[key][0], ' - ', goods[key][1], ' шт.', ' по ', goods[key][2], ' руб. ', sep='')

while True:
    try:
        num = int(input('Введите номер элемента: '))
        if num != 0:
            try:
                if str(num) in goods:
                    how_many_items = int(input('Количество: '))
                    goods[str(num)][1] += how_many_items
            except ValueError:
                print()
                print('Введите корректное значение: ')
        else:
            break
    except ValueError:
        print()
        print('Введите корректное значение: ')

for key in goods:
    print(key, ') ', goods[key][0], ' - ', goods[key][1], ' шт.', ' по ', goods[key][2], ' руб. ', sep='')