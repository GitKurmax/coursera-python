n = int(input())

if n % 10 == 1 and (n < 11 or n > 20):
    print(n, "korova")
elif n % 10 > 1 and n % 10 < 5 and (n < 11 or n > 20):
    print(n, "korovy")
else:
    print(n, "korov")
