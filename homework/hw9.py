a = input("Введите первое слово: ")
b = input("Введите второе слово: ")
c = set(a) | set(b)
for i in c:
    print(i, end=" ")

