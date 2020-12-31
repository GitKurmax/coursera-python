x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

differenceX = x1 - x2
differenceY = y1 - y2

if differenceX < 0:
    differenceX = -differenceX

if differenceY < 0:
    differenceY = -differenceY

condition1 = differenceX % 2 == 0 and differenceY % 2 == 0
condition2 = differenceX % 2 != 0 and differenceY % 2 != 0

if condition1 or condition2:
    print("YES")
else:
    print("NO")
