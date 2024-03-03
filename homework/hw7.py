from math import pi, sqrt

print("Вычисление площади фигур")
n = int(input("Выбор фигуры\n1 - треугольник\n2 - прямоугольник\n3 - круг\n: "))
if n == 1:
    a = int(input("Введите сторону a: "))
    b = int(input("Введите сторону b: "))
    c = int(input("Введите сторону c: "))
    p = (a + b + c) / 2
    print(round(sqrt(p*(p-a)*(p-b)*(p-c)), 2))
elif n == 2:
    a = int(input("Введите сторону a: "))
    b = int(input("Введите сторону b: "))
    print(a * b)
else:
    r = int(input("Введите радиус: "))
    print(round(pi * (r ** 2), 2))


