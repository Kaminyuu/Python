n = int(input("Введите число от 1 до 99: "))
if 1 <= n <= 99:
    print(n, "копе", end="")
    if n == 11 or n == 12 or n == 13 or n == 14:
        print("ек", sep="")
    elif n % 10 == 1:
        print("йка", sep="")
    elif n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
        print("йки", sep="")
    else:
        print("ек", sep="")
else:
    print("Ошибка ввода данных")
