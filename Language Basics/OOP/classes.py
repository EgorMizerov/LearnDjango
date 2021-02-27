class Book:
    # Неизменяемая переменные класса, которая будет уникальна для каждого объекта
    publisher: str = "Аноним"
    # Изменяемая переменная класса, которая будет общей для всех объектов

    # Конструктор
    def __init__(self, name):
        self.name = name


x = Book("Алиса в стране чудес")
y = Book("Гарри Потер")

print(f"Название книги X - {x.name}")
print(f"Название книги Y - {y.name}\n")

print(f"Издатель книги X - {x.publisher}")
print(f"Издатель книги Y - {y.publisher}")

x.publisher = "Oriell"

print(f"Издатель книги X - {x.publisher}")
print(f"Издатель книги Y - {y.publisher}")

# Добовление локальной переменной
x.author = "Льюис Кэрролл"
print(f"Автор книги {x.name} - {x.author}")