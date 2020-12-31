n1, n2 = int(input()), int(input())

if (n1 - 1) % (n2 - n1 + 1) == 0:
    print("Yes")
else:
    print("No")
