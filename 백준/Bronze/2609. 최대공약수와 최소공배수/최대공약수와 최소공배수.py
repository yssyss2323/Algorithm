def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


m, n = map(int, input().split())
print(gcd(m, n))
print(m * n // gcd(m, n))
