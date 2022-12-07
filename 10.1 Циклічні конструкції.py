"Циклічні конструкції"
# Циклічний алгоритм - алгоритм, що передбачає повторення однієї дії

# Види циклів:
# 1.1 Цикл з передумовою (while)
x = int(input("Number: "))
while x <= 0:
    x = int(input("Positive number: "))

# 1.2 Цикл з передумовою (while - else)
x = int(input("Number: "))
while x <= 0:
    x = int(input("Positive number: "))
else:
    print("Complete")

# 1.3 Цикл з передумовою (while - True)
x = int(input("Number: "))
while True:
    x += 1
    print(x)

# 2.1 Цикл з післяумовою - аналогічний циклу з післяумовою, тільки умова перевіряється в кінці

# 3.1 Цикл з лічильником (for - in range)
for a in range(0, 10, 2):
    print(a)

# 3.2 Цикл з лічильником (for - else)
for a in range(0, 10, 2):
    print(a)
else:
    print("Complete")

# 4.1 Вкладений цикл
for a in range(10):
    for b in range(10):
        print("*", end="")
    print()
