persons = {
    'John': {
        'N': 3056,
        'S': 8463,
        'E': 8441,
        'W': 2694,
    },
    'Tom': {
        'N': 4832,
        'S': 6786,
        'E': 4737,
        'W': 3612,
    },
    'Anne': {
        'N': 5239,
        'S': 4802,
        'E': 5820,
        'W': 1859,
    },
    'Fiona': {
        'N': 3984,
        'S': 3645,
        'E': 8821,
        'W': 2451,
    },
}

for key, value in persons.items():
    print(key)
    for letter, nums in value.items():
        print(letter, ' : ', nums)

name = input('Имя: ')

while True:
    if name in persons:
        region = input('Регион: ')
        if region in persons[name]:
            break
        else:
            print('Введите корректное значение региона.')
    else:
        print('Введите корректное имя.')
        name = input('Имя: ')

for name_person, nest_dict in persons.items():
    for key, value in nest_dict.items():
        if name_person == name and key == region:
            print(value)
            new_value = int(input('Новое значение: '))
            persons[name][region] = new_value


print(persons[name])

