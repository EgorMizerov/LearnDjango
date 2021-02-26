# Инициализацию
tel = {'jack': 4098, 'sape': 4139}

# Удалени
del tel['sape']  # {'jack': 4098}

# Изминение
tel['guido'] = 4127  # {'jack': 4098, 'guido': 4127}

tel_list = list(tel)  # ['jack', 'guido']

t = 'guido' in tel  # True

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])  # {'sape': 4139, 'guido': 4127, 'jack': 4098}

for k, v in tel.items():
    print(f"Ключ - {k}\tЗначение - {v}")