lst = [
    {
        'name': 'Антон',
        'lastname': 'Бирюков',
        'rating': 9
    },
    {
        'name': 'Алексей',
        'lastname': 'Бодня',
        'rating': 10
    },
    {
        'name': 'Федор',
        'lastname': 'Сидоров',
        'rating': 4
    },
    {
        'name': 'Михаил',
        'lastname': 'Семенов',
        'rating': 6
    }
]


# def create_dict(item):
#     cl = []
#     for elem in item:
#         cl.append(dict(elem))
#     return cl
#
#
# sort_by_name = []
#
# for el in lst:
#     sort_by_name.append(list(el.items()))
#
# sort_by_name.sort(key=lambda i: i[1])
#
# one = create_dict(sort_by_name)
# print(one)
#
# sort_by_rate_up = []
#
# for el in lst:
#     sort_by_rate_up.append(list(el.items()))
#
# sort_by_rate_up.sort(key=lambda i: i[2])
#
# two = create_dict(sort_by_rate_up)
# print(two)
#
# sort_by_rate_down = []
#
# for el in lst:
#     sort_by_rate_down.append(list(el.items()))
#
# sort_by_rate_down.sort(reverse=True, key=lambda i: i[2])
#
# three = create_dict(sort_by_rate_down)
# print(three)

# res1 = sorted(lst, key=lambda i: i['lastname'])
# res2 = sorted(lst, key=lambda i: i['rating'])
# res3 = sorted(lst, reverse=True, key=lambda i: i['rating'])
# print(res1)
# print(res2)
# print(res3)
