def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

a, b = map(int, input().split())
c, d = map(int, input().split())

e = (c * b + a * d) // gcd(b, d)
f = b * d // gcd(b, d)
print(e // gcd(e, f), f // gcd(e, f))