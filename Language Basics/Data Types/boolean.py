t = True
f = False

t1 = bool(1)    # True
f1 = bool(0)    # False

t2 = bool(" ")  # True
f2 = bool("")   # False

t3 = not False  # True
f3 = not True   # False

t4 = True and True    # True
f4 = True and False   # False
f5 = False and False  # False

t5 = True or True    # True
t6 = True or False   # True
f6 = False or False  # False

t7 = True is True    # True
t8 = False is False  # True
f7 = False is True   # False

t9 = 10 > 3  # True
f8 = 10 < 3  # False

t10 = 10 <= 10  # True
f9 = 10 >= 9    # False

t11 = 10 != 9  # True
f10 = 10 == 9  # False

t12 = True is not False  # True

t13 = "a" in ["a", "b", "c"]  # True
