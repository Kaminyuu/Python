class Car:

    def __init__(self, name, year, brand, engine, color, cost):
        self.name = name
        self.year = year
        self.brand = brand
        self.engine = engine
        self.color = color
        self.cost = cost

    def print_info(self):
        print("Данные автомобиля".center(40, "*"))
        print(f"Название модели: {self.name}\nГод выпуска: {self.year}\nПроизводитель: {self.brand}\n"
              f"Мощность двигателя: {self.engine} л.с\nЦвет машины: {self.color}\nЦена: {self.cost}")
        print("=" * 40)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_brand(self, brand):
        self.brand = brand

    def get_brand(self):
        return self.brand

    def set_engine(self, engine):
        self.engine = engine

    def get_engine(self):
        return self.engine

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_cost(self, cost):
        self.cost = cost

    def get_cost(self):
        return self.cost


p1 = Car("X7 M50i", 2021, "BMW", 530, "white", 10790000)
p1.print_info()
