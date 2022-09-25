"2.1 Рядки"
# Рядок - незмінний тип даних, використовується для збереження текстової інформації

# Робота з рядками
'Hello Ukraine'
"Hello Ukraine"
'''Hello 
        Ukraine'''
"""Hello 
        Ukraine"""
# Конкатенація - метод, який дозволяє об'єднувати декілька рядків в один
name = "Taras"
surname = "Shevchenko"
message = "Hi! My name is " + name + "! ""My surname is " + surname + "!"
print(message)

# Інтерполяція - метод, який дозволяє вставляти зміні в рядок
name = "Taras"
surname = "Shevchenko"
message = f"Hi! My name is {name}! My surname is {surname}!"
print(message)
