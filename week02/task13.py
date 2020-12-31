# Даны три стороны треугольника a,b,c. Определите тип треугольника
#  с заданными сторонами. Выведите одно из четырех слов: rectangular
# для прямоугольного треугольника, acute для остроугольного
# треугольника, obtuse для тупоугольного треугольника или impossible,
#  если треугольника с такими сторонами не существует (считаем, что
# вырожденный треугольник тоже невозможен).

# Формат ввода

# Вводятся три целых числа.
a, b, c = int(input()), int(input()), int(input())

if a >= b and a >= c:
    max = a
    min1 = b
    min2 = c
elif b >= a and b >= c:
    max = b
    min1 = a
    min2 = c
else:
    max = c
    min1 = a
    min2 = b

res = min1**2 + min2**2

if res == max**2:
    print("rectangular")
elif res > max**2:
    print("obtuse")
elif res < max**2:
    print("acute")
else:
    print("impossible")
