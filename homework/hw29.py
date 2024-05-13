class ValidInt:

    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if value <= 0:
            raise TypeError(f"{self.__name} должно быть положительным числом")
        instance.__dict__[self.__name] = value


class Order:
    cost = ValidInt()
    quantity = ValidInt()

    def __init__(self, name, cost, quantity):
        self.name = name
        self.cost = cost
        self.quantity = quantity

    def total(self):
        return self.cost * self.quantity


print("Тест: ")
o = Order('apple', 5, 10)
print(f"{Order.__name__}('{o.name}', {o.cost}, {o.quantity})")
# print(o.__dict__)
print(o.total())
