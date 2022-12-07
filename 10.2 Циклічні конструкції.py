"Циклічні конструкції"
# Оператори
# 1. break
while True:

    print("Login:")
    a = input(">")

    if a == "ABC":
        break

# 2. continue
x = 0
while x < 10:
    x += 1
    if x == 5:
        continue
    print(x)
