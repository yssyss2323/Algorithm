def solv(point1, point2, point3):
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3
    return (y2 - y1) * (x3 - x2) + (x1 - x2) * (y3 - y2) == 0


points = [list(map(int, input().split())) for _ in range(3)]
if solv(points[0], points[1], points[2]):
    print("WHERE IS MY CHICKEN?")
else:
    print("WINNER WINNER CHICKEN DINNER!")