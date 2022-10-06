"5.3 Sequence Type (list)"
a = [3, 56, 2, 7, 9]
print(a)

# Методи:
# .append() - додає 1 елемент в кінець списку
a.append(3)
print(a)

# .extend() - додавання декількох елементів до списку
a.extend([4, 1])
print(a)

# .insert() - вставлення елемента в список за індексом
a.insert(0, 2)
print(a)

# .copy() - копіювання списку
a.copy()
print(a)

# .count() - підраховує кількість певних елементів
print(a.count(3))

# .index() - отримання індекса елемента
print(a.index(7))

# .reverse() - повертає обернений список
a.reverse()
print(a)

# .sort() - сортує список за зростанням, змінюючи вихідний
a.sort()
print(a)

# .sort(reverse=True) - сортує список за спаданням, змінюючи вихідний
a.sort(reverse=True)
print(a)

# .pop() - видаляє елемент з кінця або за індексом
a.pop()
print(a)
a.pop(2)
print(a)

# .remove() - видаляє заданий елемент списку
a.remove(3)
print(a)

# .clear() - повністю очищує список
a.clear()
print(a)
