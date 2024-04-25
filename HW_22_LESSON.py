math_olimp = {'Matvei', 'Evgeniya', 'Michail', 'Maxim', 'Natalia'}
math_phisics = {'Maxim', 'Matvei', 'Alexandr'}

all_persons = math_olimp | math_phisics
print('Все призёры: ', list(all_persons))

winners_both_olimps = math_olimp & math_phisics

print('Призеры обеих олимпиад: ', winners_both_olimps)

math_olimp &= math_phisics

print('Обновленный список призеров по математике: ', math_olimp)