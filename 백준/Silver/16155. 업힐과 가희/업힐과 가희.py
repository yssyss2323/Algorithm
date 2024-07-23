def find_line(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    a = y2 -y1
    b = x1 -x2
    c = x2 * y1 - x1 * y2
    return -a, -b, -c

def gcd(x,y):
    if y == 0:
        return x
    return gcd(y, x % y)

n = int(input())
#x0, h0 = map(int, input().split())
checkpoint = [list(map(int, input().split())) for _ in range(n + 1)]
s, e = map(int, input().split())

y_points = [-1, -1]
for i in range(n):
    point1 = checkpoint[i]
    point2 = checkpoint[i + 1]
    if y_points[0] == -1 and point1[0] <= s < point2[0]:
        a,b,c = find_line(point1, point2)
        y_points[0] = [-a * s - c, b]
    if y_points[1] == -1 and point1[0] < e <= point2[0]:
        a, b, c = find_line(point1, point2)
        y_points[1] = [-a * e - c, b]
numerator = abs(y_points[0][1] * y_points[1][0] - y_points[0][0] * y_points[1][1])
denominator = abs(y_points[0][1] * y_points[1][1] * (e - s))
if numerator % denominator == 0:
    print(numerator // denominator)
else:
    gcd = gcd(numerator, denominator)
    numerator //= gcd
    denominator //= gcd
    print(f"{numerator}/{denominator}")