# print('Создал сам репозиторий')

# закомментировал принт

# a = {1, 2}
# b = {3}
# c = {4, 5}
# d = {3, 2, 6}
# e = {6}
# f = {7, 8}
# g = {9, 8}
#
# clean_set = a | b | c | d | e | f | g
#
# print(clean_set)
# print('Unic elems count:', len(clean_set))
# print('Min elem:', min(clean_set))
# print('Max elem:', max(clean_set))

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core i5-3450', 5, 6400],
# }
#
# for key in goods:
#     print(key, ') ', goods[key][0], ' - ', goods[key][1], ' шт.', ' по ', goods[key][2], ' руб. ', sep='')
#
# dict = {}
#
# while True:
#     n = input('№ ')
#     if n != '0':
#         how_many = int(input('Количество: '))
#         dict[n] = how_many
#     else:
#         break
#
# for el in dict:
#     if el in goods:
#         goods[el][1] = dict[el]
#
#
# for key in goods:
#     print(key, ') ', goods[key][0], ' - ', goods[key][1], ' шт. по ', goods[key][2], ' руб.', sep='')
