
with open('test', 'r') as f:
    title = f.readline()
    body = f.read()

print(f"Загаловок - {title}")
print(f"Всё остольное:\n{body}")

f.close()

with open("test", 'r') as f:
    print("Файл цеелком:")
    for i in f:
        print(i, end='')

f.close()
