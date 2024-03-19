str1 = "Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интересный язык программирования."
str2 = ""

for x in str1:
    if x == "N":
        str2 += "P"
    else:
        str2 += x

print(str1)
print(str2)


