def distance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5

Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = map(int, input().split())

a = Cx - Ax
b = (Dx - Cx) - (Bx - Ax)
c = Cy - Ay
d = (Dy - Cy) - (By - Ay)

if b ** 2 + d ** 2 == 0:
    t = 0
else:
    t = - (a * b + c * d) / (b ** 2 + d ** 2)

if t < 0:
    t = 0
elif t > 1:
    t = 1

point1 = (Ax + (Bx - Ax) * t, Ay + (By - Ay) * t)
point2 = (Cx + (Dx - Cx) * t, Cy + (Dy - Cy) * t)

print(distance(point1, point2))
