def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

while True:
    x1, y1, x2, y2, x3, y3 = map(int,input().split())
    if (x1, y1, x2, y2, x3, y3) == (0, 0, 0, 0, 0, 0):
        break
    a = abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2)
    b = gcd(abs(x2 - x1), abs(y2 - y1)) + gcd(abs(x3 - x2), abs(y3 - y2)) + gcd(abs(x1 - x3), abs(y1 - y3))
    ans = (a - b + 2) // 2
    print(ans)