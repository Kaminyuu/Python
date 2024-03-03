num = int(input("Введите пятизначное число: "))

a = num % 10
b = (num % 100) // 10
c = (num % 1000) // 100
d = (num % 10000) // 1000
e = (num % 100000) // 10000

summ = a * b * c * d * e
aver = (a + b + c + d + e) / 5
print("Произведение цифр числа ", num, ": ", summ, sep="")
print("Среднее арифметическое:", aver)
