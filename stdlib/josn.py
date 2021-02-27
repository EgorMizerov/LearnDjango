import json

kw = {"Egor": {"age": 18, "height": 175.0, "mother": "Olga"}, "Alisa": {"age": 16, "height": 165.0, "mother": "Olga"}}

# Сериализация
string = json.dumps(kw)
print(string)

# Записываем JSON в файл
with open("kw.json", "w") as f:
    json.dump(kw, f)
f.close()

# Читаем из файла
with open("kw.json", "r") as f:
    data = json.load(f)
f.close()

print(data)

