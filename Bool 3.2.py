"3.2 таблиця істиності логічних операцій"
# 1. not (не)
# not True = False
print(not 5 < 7)

# not False = True
print(not 45 <= 32)

# 2. and (і)
# True and True = True
print(34 > 23 and 45 >= 21)

# True and False = False
print(5 == 5 and 7 != 7)

# False and True = False
print(24 < 12 and 23 <= 34)

# False and False = False
print(65 > 92 and 95 >= 99)

# 3. or (або)
# True or True = True
print(8 == 8 or 25 != 4)

# True or False = True
print(23 < 47 or 38 <= 21)

# False or True = True
print(34 > 29 or 67 >= 49)

# False or False = False
print(23 == 34 or 43 != 43)
