# print('Создал сам репозиторий')

# закомментировал принт

a = {1, 2}
b = {3}
c = {4, 5}
d = {3, 2, 6}
e = {6}
f = {7, 8}
g = {9, 8}

clean_set = a | b | c | d | e | f | g

print(clean_set)
print('Unic elems count:', len(clean_set))
print('Min elem:', min(clean_set))
print('Max elem:', max(clean_set))