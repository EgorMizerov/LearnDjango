def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


for char in reverse('golf'):
     print(char)

# Генераторы выражения
print(sum(i*i for i in range(10)))

xvec = [10, 20, 30]
yvec = [7, 5, 3]

print(sum(x*y for x, y in zip(xvec, yvec)))
