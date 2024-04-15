import math


class Shapes:
    count = 0

    @staticmethod
    def heron_formula(a, b, c):
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        Shapes.count += 1
        return s

    @staticmethod
    def triangle_formula(a, h):
        s = 0.5 * a * h
        Shapes.count += 1
        return s

    @staticmethod
    def square_formula(a):
        s = a ** 2
        Shapes.count += 1
        return s

    @staticmethod
    def rectangle_formula(a, b):
        s = a * b
        Shapes.count += 1
        return s

    @staticmethod
    def get_count():
        return Shapes.count


print(f"Площадь треугольника по формуле Герона (3, 4, 5): {Shapes.heron_formula(3, 4, 5)}")
print(f"Площадь треугольника через основание и высотку (6, 7): {Shapes.triangle_formula(6, 7)}")
print(f"Площадь квадрата (7): {Shapes.square_formula(7)}")
print(f"Площадь прямоугольника (2, 6): {Shapes.rectangle_formula(2, 6)}")
print(f"Количество подсчета площади: {Shapes.get_count()}")
