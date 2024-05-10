def distance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2 + (point2[2] - point1[2]) ** 2) ** 0.5

Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz = map(int,input().split())

t = ((Ax - Cx) * (Ax - Bx) + (Ay - Cy) * (Ay - By) + (Az - Cz) * (Az - Bz)) / ((Bx - Ax)**2 + (By - Ay)**2 + (Bz - Az)**2)
if t > 1:
    t = 1
if t < 0:
    t = 0

point = (Cx, Cy, Cz)
check_point = (Ax + (Bx - Ax) * t, Ay + (By - Ay) * t, Az + (Bz - Az) * t)

answer = distance(point, check_point)
print(answer)