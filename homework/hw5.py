print("Введите элементы списка:")
a = [int(input("-> ")) for i in range(int(input("n = ")))]
k = int(input("Введите индекс: "))

if k > len(a) or k == len(a):
    print("Введен неверный индекс")
else:
    a.pop(k)
    print("k =", k)
    print(a)

