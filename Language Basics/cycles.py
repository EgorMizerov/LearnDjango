lst = [1, 2, 3, 4, 5]
kw = {"Егор": "+79028055083", "Ольга": "+79028052228", "Алиса": "+79028383624"}

rg1 = range(5)         # (0, 1, 2, 3, 4)
rg2 = range(0, 5)      # (0, 1, 2, 3, 4)
rg3 = range(0, 10, 2)  # (0, 2, 4, 6, 8)


# Цикл While
i = 0

print("Цикл while")
while i < len(lst):
    print(lst[i])
    i += 1


# Цикл For
print("Цикл for по списку")
for i in lst:
    print(i)

print("Цикл for по словарю")
for key, value in kw.items():
    print("Номер телефона %s - %s" % (key, value))


# Операторы break, continue и pass
print("Цикл с операторами")
for i in rg1:
    if i == 0:
        # Ничего не происходит
        pass
    if i == 2:
        print("Число 2 пропускаем")
        # Пропускается иттерация
        continue
    if i == 4:
        print("4 - конечное число")
        # Заканчивается цикл
        break

    print(i)
