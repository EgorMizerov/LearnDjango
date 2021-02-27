# Определение функций

def fib(n):
    """Функция вычисляет последовательность фиббоначчи"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b

    return result


# Функция обязательно должна принимать первый параметр и не оязательно последующие 2
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    """Функция подтверждения действия"""
    while True:
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')

        ok = input(prompt + " ")

        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False

        print(reminder)


def cheese_shop(kind, *arguments, **keywords):
    """Функция выводит список аргументов"""
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


# До / идут позиционные аргументы, а после * по клчевым словам
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    pass


# Аннотации
def people_str(name: str, age: int) -> str:
    return f"Имя: {name}\tВозраст - {age}"


# Лямбда выражения
pow_x_y = lambda x, y: x * y

ask_ok("Do you really want to quit?", 2, "Ппробуйте ещё раз")
cheese_shop('Hello', 1, True, name="Egor", age=18)
f(1, 2, pos_or_kwd=3, kwd1=5, kwd2=20)
print(pow_x_y(4, 2))
print(people_str.__annotations__)


def scope_test():
    def do_local():
        # Не видна из вне
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        # Видна внтури функции
        spam = "nonlocal spam"

    def do_global():
        global spam
        # Видна изнутри
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)
