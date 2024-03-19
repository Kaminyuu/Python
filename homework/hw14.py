def avg(fn):
    def wrap(*args):
        print("Сумма чисел 2, 3, 3, 4 =", fn(*args))
        print("Среднее арифметическое 2, 3, 3, 4 =", fn(*args) / len(args))

    return wrap


@avg
def summ(*args):
    return sum(args)


summ(2, 3, 3, 4)

# def avg(fn):
#     def wrap(*args):
#         return fn(*args) / len(args)
#
#     return wrap
#
#
# @avg
# def summa(*args):
#     return sum(args)
#
#
# print(summa(2, 3, 3, 4))
