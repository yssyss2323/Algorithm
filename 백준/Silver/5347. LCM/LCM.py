def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a * b // gcd(a, b))