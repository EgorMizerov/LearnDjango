print("Ввведите число: ")
choice = int(input())

value = 10

if choice > value:
    print("%d больше %d" % (choice, value))
elif choice < value:
    print("%d меньше %d" % (choice, value))
else:
    print("%d равен %d" % (choice, value))
