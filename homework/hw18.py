def negative(lst):
    count = 0
    for i in lst:
        if i < 0:
            count += 1
            negative(lst[1:])
        else:
            negative(lst[1:])
    return count


print("n =", negative([-2, 3, 8, -11, -4, 6]))
