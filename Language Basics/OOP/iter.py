class Library:
    def __init__(self, books: list[str]):
        self.books = books
        self.index = len(books)

    # Вызывается при for i in Library
    def __iter__(self):
        return self

    # Вызывается каждую иттерацию
    def __next__(self):
        if self.index == 0:
            self.index = len(self.books)
            raise StopIteration

        self.index = self.index - 1

        return self.books[self.index]


lib = Library(["Гарри Потре", "Алиса в стране чудес", "Волк и семеро козлят"])

for i in lib:
    print(i)
