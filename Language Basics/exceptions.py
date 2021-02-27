
try:
    x = int(input("Please enter a number: "))
except ValueError:
    print("Oops!  That was no valid number.  Try again...")
else:
    print("Без ошибок!")
finally:
    print("Это неменуемо произойдёт!")

try:
    # raise - вызов ошибки
    raise Exception("Специальное предуприждение!")
except Exception:
    print(Exception)


class MyError(Exception):
    """My Error"""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "Собственная ошибка"


try:
    raise MyError("Моя ошбика!")
except MyError as err:
    print(err)
