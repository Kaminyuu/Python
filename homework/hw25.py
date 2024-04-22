# class Student:
#     def __init__(self, name):
#         self.name = name
#
#     class Computer:
#         def __init__(self, model, cpu, ram, obj):
#             self.model = model
#             self.cpu = cpu
#             self.ram = ram
#             self.obj = obj
#
#         def display(self):
#             print(f"{self.obj.name} => {self.model}, {self.cpu}, {self.ram}")
#
#
# name1 = Student("Roman")
# pc1 = name1.Computer("HP", "i7", 16, name1)
# pc1.display()


class Student:
    def __init__(self, name):
        self.name = name
        self.obj = self.Computer()

    def show(self):
        print(f"{self.name} => {self.obj.model}, {self.obj.cpu}, {self.obj.ram}")

    class Computer:
        def __init__(self):
            self.model = "HP"
            self.cpu = "i7"
            self.ram = 16


name1 = Student("Roman")
name1.show()
pc1 = name1.obj
name2 = Student("Vladimir")
name2.show()
pc2 = name2.obj
