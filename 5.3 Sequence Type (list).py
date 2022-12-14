"5.3 Sequence Type (list)"
# Список - змінний тип даних, що є впорядкованою послідовністю певних значень

# Створення списків
# 1
a = [3, 56, 2, 7, 9]
print(a)

# 2
b = ['a', "b", 'HELLO']
print(b)

# 3
c = [56, 8, 'world', 34.87]
print(c)

# 4
d = []
print(d)

# 5
e = list()
print(e)

# Операції зі списками:
# a + b - складання
print(a + c)

# a * 2 - дублювання
print(b * 2)

# >,<,>=,<=,==,! - порівняння
print(a == b)

# in - перевіряє чи є елемент у списку
print(56 in a)

# len() - довжина списку
print(len(c))

# min() - виводить мінімальне значення в списку
print(min(a))

# max - виводить максимальне значення в списку
print(max(b))

# sum - сума елементів
print(sum(a))
