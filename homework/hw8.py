from random import randint


def tuple_creator(a, b):
    tpl = tuple(randint(a, b) for i in range(10))
    print(tpl)
    return tpl


# tpl1 = tuple_creator(0, 5)
# tpl2 = tuple_creator(-5, 0)
tpl3 = tuple_creator(0, 5) + tuple_creator(-5, 0)
print(tpl3)
print("0 =", tpl3.count(0))
