import random

w, h = 3, 4
matrix = [[random.randint(-20, 10) for x in range(w)] for y in range(h)]
count = 0
for row in matrix:
    for x in row:
        print(x, end="\t\t")
        if x < 0:
            count += 1
    print()

print("Количество отрицательных элементов:", count)


