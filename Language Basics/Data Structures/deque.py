from collections import deque

# Инициализация очереди
queue = deque(["Егор", "Алиса", "Ольга"])

# Добовление элемента
queue.append("Денис")

# Извлечение элемента
queue.popleft()
