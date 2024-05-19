person_fullname = list(map(lambda x: x[0].upper() + x[1:].lower(), input('Введите ФИО: ').split()))

for i in range(len(person_fullname)):
    if i > 0:
        person_fullname[i] = person_fullname[i][:1] + '.'

print(person_fullname)

FIO = ' '.join(person_fullname)
print(FIO)