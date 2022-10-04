"5.1 Sequence Type (namedtuple)"
# Іменований кортеж - це заміна звичайних кортежів, що виконують ті ж функції, але покращують читаність коду.

# Створення іменованого кортежу
from collections import namedtuple
Human = namedtuple("Person", "name surname") # створення class з атрибутами
a = Human("Тарас", "Шевченко")
print(a)
print(a[1]) # виклик за індексом 
print(a.name) # виклик за атрибутом
