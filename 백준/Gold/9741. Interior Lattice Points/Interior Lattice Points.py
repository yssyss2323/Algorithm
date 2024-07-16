def gcd(x,y):
    if y == 0:
        return x
    return gcd(y, x % y)

def point_on_line(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    x, y = abs(x1 - x2), abs(y1 - y2)
    if x == 0:
        return y
    elif y == 0:
        return x
    else:
        return gcd(x, y)

n = int(input())
for _ in range(n):
    xa, ya, xb, yb, xc, yc = map(int, input().split())
    s = abs(xa * yb + xb * yc + xc * ya - xb * ya - xc * yb - xa * yc) / 2
    if s == 0:
        print(0)
    else:
        y = point_on_line((xa,ya), (xb,yb)) + point_on_line((xb,yb),(xc,yc)) + point_on_line((xc,yc), (xa,ya))
        print(int(s + 1 - y / 2))