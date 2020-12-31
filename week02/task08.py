n, m, k = int(input()), int(input()), int(input())

total = n * m

if k <= total and (k % n == 0 or k % m == 0):
    print("YES")
else:
    print("NO")
