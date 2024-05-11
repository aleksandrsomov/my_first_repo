def calc_average(fn):
    def wrap(*args):
        message = 'чисел '
        for el in args:
            message += str(el) + ', '

        message = message[0: -2]

        print('Сумма', message, '=', fn(*args))
        return fn(*args) / len(args)
        # print('Среднее арифметическое', message, '=', average)

    return wrap


@calc_average
def summa(*args):
    return sum(args)


print('Среднее арифметическое чисел', summa(2, 3, 3, 4))
