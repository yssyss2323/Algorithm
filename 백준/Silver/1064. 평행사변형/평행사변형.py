def distance(point1, point2):
    x_square = (point1[0] - point2[0]) ** 2
    y_square = (point1[1] - point2[1]) ** 2
    return (x_square + y_square) ** 0.5

def is_line(point1, point2, point3):
    if point1[0] == point2[0] == point3[0]:
        return True
    if point1[1] == point2[1] == point3[1]:
        return True
    a = point2[1] - point1[1]
    b = point1[0] - point2[0]
    c = point1[0] * (point2[1] - point1[1]) + point1[1] * (point1[0] - point2[0])
    return a * point3[0] + b * point3[1] == c

x1, y1, x2, y2, x3, y3 = map(int, input().split())
point1 = (x1, y1)
point2 = (x2, y2)
point3 = (x3, y3)

if is_line(point1, point2, point3):
    print(-1)
else:
    dist = [distance(point1, point2), distance(point2, point3), distance(point3, point1)]
    dist.sort()
    print((dist[2] - dist[0]) * 2)