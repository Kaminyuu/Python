n = int(input("Количество символов: "))
m = input("Тип символа: ")
print("0 - горизонтальная линия")
print("1 - вертикальная линия")
l = int(input("Ориентация линии: "))

for i in range(n):
    if l == 0:
        print(m, end=" ")
    elif l == 1:
        print(m)
else:
    print("Введите корректную ориентацию!")


