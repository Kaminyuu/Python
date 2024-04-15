class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @name.deleter
    def name(self):
        del self.__name

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, new_old):
        self.__old = new_old

    @old.deleter
    def old(self):
        del self.__old


p1 = Person("Irina", 26)
print(p1.__dict__)
p1.name = "Igor"
print(p1.name)
p1.old = 31
print(p1.old)
p1.old = 26
del p1.name
print(p1.__dict__)
