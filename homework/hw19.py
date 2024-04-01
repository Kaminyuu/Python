text = "Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n"


def change(file):
    with open(file, "w") as f:
        f.write(text)
    try:
        pos1 = int(input("pos1 = "))
        pos2 = int(input("pos2 = "))
        with open(file, "r") as f:
            a = f.readlines()
            a[pos1], a[pos2] = a[pos2], a[pos1]
        with open(file, "w") as f:
            f.writelines(a)
    except (ValueError, IndexError):
        print("Введены некорректные индексы или таких индексов не существует, изменения в файле не будут внесены")


change("test1.txt")
