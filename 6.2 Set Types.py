"6.2 Set Types"
a = {2, 43, 3, 9, 7}
b = {41, 3, 65, 7}
# Методи:
# .add() - додає елемент до множини
a.add(1)
print(a)

# .update() - додає декілька елементів до множини
a.update([5, 8])
print(a)

# .discard() - видаляє елемент, якщо нема виводить множину
a.discard(3)
b.discard(4)
print(a)
print(b)

# .remove() - видаляє елемент, якщо нема виводить KeyError
a.remove(2)
b.remove(87)
print(a)
print(b)

# .clear() - видаляє всі елементи з множини
a.clear()
print(a)

# .union() - обєднує множини
print(a.union(b))
