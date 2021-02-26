from typing import Optional, Any, Union, List, Tuple, Dict, NoReturn

# Аннотации переменных
number: int  # Только int
age: float
title: str
cond: bool

number2: Optional[int]  # int или None
something: Any  # Что угодно
union: Union[int, float]  # Либо int, либо float
lst: List[int]  # Список целых чисел
tpl: Tuple[int]  # Кортеь целых чисел
dct: Dict[str, int]  # Словарь, где ключ - строка, значение - целове число


# Аннотация функций
def f(n: int, s: str) -> bool:
    pass


# Аннотация класса
class Book:
    title: str
    author: str

    def __init__(self, name: str, author: str) -> NoReturn:
        self.title = name
        self.author = author


# Вывод аннотации класса и его методов
print(Book.__annotations__)
print(Book.__init__.__annotations__)

# Вывод аннотации функции
print(f.__annotations__)

# Вывод аннотации переменных
print(__annotations__)
