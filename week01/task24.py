# В этой задаче необходимо проверить, делится ли число A на число B нацело. Использовать можно только арифметические операции, использование любых видов ветвлений, функций и т.п. запрещено.

# Формат ввода

# Вводятся два натуральных числа A и B.

# Формат вывода

# Выведите "YES", если A кратно B и "NO" в противном случае.

A, B = int(input()), int(input())

print("Yes" * 0**(A % B), "No" * (1 - 0**(A % B)), sep='')
