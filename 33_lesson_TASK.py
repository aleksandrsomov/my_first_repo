s = 'Test string for me'
lst = []

for letter in s:
    lst.append(ord(letter))


def calc_avg(arr):
    """
    Функция для подсчета среднего арифметического чисел


    Функция для подсчета среднего арифметического чисел, разделяем общую сумму на кол-во элементов


    :param arr: список с числами
    :return: возвращает среднее арифметическое
    """
    return int(sum(arr) / len(arr))


print('ASCII коды: ', lst)

lst.insert(0, (calc_avg(lst)))
print('Среднее арифметическое', lst)

new_items = input('Введите еще 3 любых символа: ')
print(new_items)

for el in new_items[:3]:
    if el not in s:
        print(el)
        lst.append(ord(el))

print(lst)
print('Количество последних элементов: ', lst.count(lst[-1]))

lst.sort(reverse=True)
print(lst)
