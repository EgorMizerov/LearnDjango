# Set - список с уникальными элементами

# Инициализация
basket = {'apple', 'orange', 'apple', 'orange', 'banana'}  # {'apple', 'orange', 'banana'}

a1 = set('abracadabra')  # {'a', 'r', 'b', 'c', 'd'}

# set comprehension
a2 = {x for x in 'abracadabra' if x not in 'abc'}  # {'r', 'd'}
