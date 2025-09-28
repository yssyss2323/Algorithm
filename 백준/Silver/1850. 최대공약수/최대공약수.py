def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

a, b = map(int, input().split())
cnt = gcd(a, b)
print('1' * cnt)