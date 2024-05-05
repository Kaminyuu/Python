from abc import ABC, abstractmethod
from math import sqrt


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def get_perimeter(self):
        ...

    @abstractmethod
    def get_area(self):
        ...

    @abstractmethod
    def get_art(self):
        ...

    def info(self):
        print(f"Цвет: {self.color}")


class Square(Shape):
    def __init__(self, side1, color):
        self.side1 = side1
        super().__init__(color)

    def get_perimeter(self):
        return self.side1 * 4

    def get_area(self):
        return self.side1 * self.side1

    def get_art(self):
        for i in range(self.side1):
            print("*" * self.side1)

    def info(self):
        print(f"===Квадрат=== \nСторона: {self.side1}")
        super().info()
        print(f"Периметр: {self.get_perimeter()} \nПлощадь: {self.get_area()}")
        self.get_art()


class Rectangle(Shape):
    def __init__(self, side1, side2, color):
        self.side1 = side1
        self.side2 = side2
        super().__init__(color)

    def get_perimeter(self):
        return 2 * (self.side1 + self.side2)

    def get_area(self):
        return self.side1 * self.side2

    def get_art(self):
        for i in range(self.side1):
            print("*" * self.side2)

    def info(self):
        print(f"===Прямоугольник=== \nДлина: {self.side1} \nШирина: {self.side2}")
        super().info()
        print(f"Периметр: {self.get_perimeter()} \nПлощадь: {self.get_area()}")
        self.get_art()


class Triangle(Shape):
    def __init__(self, side1, side2, side3, color):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        super().__init__(color)

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def get_area(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        return round(sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side2)), 2)

    def get_art(self):
        for i in range(self.side2):
            print(" " * (self.side2 - 1 - i) + "*" * (1 + i * 2))

    def info(self):
        print(f"===Треугольник=== \nСторона 1: {self.side1} \nСторона 2: {self.side2} \nСторона 3: {self.side3}")
        super().info()
        print(f"Периметр: {self.get_perimeter()} \nПлощадь: {self.get_area()}")
        self.get_art()


s1 = Square(3, "red")
s1.info()
print()
s2 = Rectangle(3, 7, "green")
s2.info()
print()
s3 = Triangle(11, 6, 6, "yellow")
s3.info()
