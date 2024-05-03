how_many_students = input('Количество студентов: ')

while True:
    if type(how_many_students) == str:
        try:
            how_many_students = int(how_many_students)
        except ValueError:
            how_many_students = input('Введите кол-во студентов числом...')
    if type(how_many_students) == int:
        break

names = []
scores = []

for num_of_student in range(1, how_many_students + 1):
    name_person = input(f'{num_of_student}-й студент: ')
    score_num = input('Балл: ')
    while True:
        try:
            score_num = int(score_num)
        except ValueError:
            score_num = input('Введите кол-во баллов целым числом: ')
        if type(score_num) == int:
            break
    scores.append(score_num)
    names.append(name_person)


def calc_average(scores):
    return sum(scores) / len(scores)


average = round(calc_average(scores))

all_persons_dict = dict(zip(names, scores))

print()
print('Средний балл: ', average)
print('Студенты с баллом выше среднего: ')

for k, v in all_persons_dict.items():

    if v > average:
        print('Имя: ', k)
