"2.2 Методи рядків"

a = "Hello Ukraine"

# 1 .upper() - повертає рядок, де всі символи написані у верхньому регістрі
print("hello Ukraine".upper())

# 2 .lower() - повертає рядок, де всі символи написані в нижньому регістрі
print("HELLO UKRAINE".lower())

# 3 .count() - здійснює підрахунок заданих символів в даній строкі
print(a.count("o"))
print(a.count("o", 1))
print(a.count("o", 1,  8))

# 4 .find() - знаходить індекс першого заданого елемента починаючи з ліва
# в разі відсутності виводить значення -1
print(a.find("e"))
print(a.find("e", 5))
print(a.find("e", 0, 8))
print(a.find("t", 0, 8))

# 5 .rfind() - знаходить індекс першого заданого елемента починаючи з права
# в разі відсутності виводить значення -1
print(a.rfind("e"))
print(a.rfind("e", 5))
print(a.rfind("e", 0, 8))
print(a.rfind("t", 0, 8))

# 6 .index() - знаходить індекс першого заданого елемента починаючи з ліва
# в разі відсутності виводить значення ValueError
print(a.index("e"))
print(a.index("e", 5))
print(a.index("e", 0, 8))
print(a.index("m", 0, 8))

# 7 .replace() - заміна символу в строкі
print(a.replace("e", "o"))
print(a.replace("e", "o", 2))

# 8 .split() - перетворює строку в список
print(a.split())

# 9 .isalpha() - перевіряє чи складається строка з букв
print(a.isalpha())

# 10 .isdigit() - перевіряє чи складається строка з цифр
print(a.isdigit())
