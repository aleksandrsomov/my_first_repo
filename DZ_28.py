S = 0


def square_parallelepiped(a, b, c):
    global S
    S = 2 * (a * b + a * c + b * c)

    def square_rectangle():
        global S
        S = a * b

    return square_rectangle


outer_func = square_parallelepiped(1, 6, 8)  # это я создаю переменную , чтобы потом получить доступ к inner function

square_parallelepiped(2, 4, 6)  # это плошадь паралеллепипеда

outer_func()  # это плошадь прямоугольника

print(S)