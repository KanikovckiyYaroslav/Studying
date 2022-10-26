"Mappig Types"
a = {
    "B": 1,
    "C": 2,
    "D": 3
}
print(a)

# Методи:
# .pop() - видаляє та виводить словник
a.pop("C")
print(a)

# .get() - виводить значення за ключем
print(a.get("B"))

# .setdefault() - отримує значення за ключем та створює ключ-значення
print(a.setdefault("D"))
a.setdefault("C", 2)
print(a)

# .keys() - виводить всі ключі
print(a.keys())

# .values() - виводить всі значення
print(a.values())

# .items() - виводить всі ключ-значення
print(a.items())

# .clear() - видаляє всі елементи
a.clear()
print(a)
