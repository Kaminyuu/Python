class Figure:
    def __init__(self, color):
        self.color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, c):
        self.__color = c


class Rectangle(Figure):
    def __init__(self, width, height, color):
        # if width > 0 and height > 0:
        self.width = width
        self.height = height
        super().__init__(color)
        # else:
        #     raise TypeError("Площадь не может быть отрицательной")

    @staticmethod
    def verify_width(width):
        if width < 1:
            raise TypeError("Длина должна быть больше 0")

    @staticmethod
    def verify_height(height):
        if height < 1:
            raise TypeError("Ширина должна быть больше 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.verify_width(width)
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.verify_height(height)
        self.__height = height

    def area(self):
        print(f"Прямоугольник {self.color}. Площадь: ", end="")
        return self.__width * self.__height


rect = Rectangle(10, 20, "green")
print(rect.area())
