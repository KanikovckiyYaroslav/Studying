"6.1 Set Types"
# Множина - незмінний тип даних, невпорядкований набір елементів.

# Створення множин:
# 1
a = {1, 3, 45, 8, 2}
b = {"s", "drf", "dw"}
c = {34, 32, "re", "rj"}
print(a, type(a))
print(b, type(b))
print(c, type(c))

# 2
a = set("1836457383 76")
b = set("helloUkraine")
c = set("dkjffd23398")
print(a, type(a))
print(b, type(b))
print(c, type(c))

# 3
a = set([1, 4, 57])
b = set(["helloUkraine"])
c = set(["dkjffd23398"])
print(a, type(a))
print(b, type(b))
print(c, type(c))

# 4
a = set(range(9))
print(a)

# 5
a = set()
print(a)
