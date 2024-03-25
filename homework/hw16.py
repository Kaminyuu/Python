st = "Ежевику для ежат\nПринесли два ежа.\nЕжевику еле-еле\nЕжата возле ели съели."
count = 0
splt = st.split()
for i in splt:
    if i.startswith("Е") or i.startswith("е"):
        count += 1
print("Тестовый пример: ")
print(f"{st} ({count} слов)")
print()
print(f"Количество слов: {count}")
