# Даны координаты двух точек на плоскости, требуется определить,
# лежат ли они в одной координатной четверти или нет
# (все координаты отличны от нуля).

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1 > 0 and x2 < 0) or (y1 > 0 and y2 < 0):
    print("NO")
elif (x1 < 0 and x2 > 0) or (y1 < 0 and y2 > 0):
    print("NO")
else:
    print("YES")
