def func(*args):
    dic = {}
    for i in args:
        dic[i] = i
    return dic


print(func(1, 2, 3, 4))
print(func('grey', (2, 17), 3.11, -4))
