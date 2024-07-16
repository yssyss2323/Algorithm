import sys
input = sys.stdin.readline

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

n,m,p = map(int, input().split())
points = [(0,0), (n,m), (p,0), (0,0)]
a1, a2 = 0, 0
y = 0
for i in range(3):
    a1 += points[i][0] * points[i+1][1]
    a2 += points[i][1] * points[i+1][0]
    y += point_on_line(points[i], points[i+1])
s = abs(a1 - a2) / 2
print(int(s + 1 - y / 2))