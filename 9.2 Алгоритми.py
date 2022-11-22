"Алгоритми"
# Оператори розгалуження
# 1. if
x = 7
if x > 0:
    print("A")

# 2. if - else
x = -2
if x > 0:
    print("A")
else:
    print("B")

# 3. if - elife - else
x = 0
if x > 0:
    print("A")
elif x < 0:
    print("B")
else:
    print("C")

# 4. Тернарний оператор - більш компактна форма запису умовних конструкцій
x = 5
print("A" if x > 0 else "B")

# 5. match\case
day = "вівторок"
match day:
    case "понеділок":
        print("Преший день")
    case "вівторок":
        print("Другий день")
    case "середа":
        print("Третій день")
