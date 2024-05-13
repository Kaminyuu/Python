class Square:
    def __init__(self, a):
        self.a = a

    def get_perimeter(self):
        return 4 * self.a


if __name__ == '__main__':
    print("Код в документе sq.py")
    s1 = Square(10)
    s2 = Square(20)
    print("Код из документа sq.py:", s1.get_perimeter())
    print("Код из документа sq.py:", s2.get_perimeter())
