from math import pi

def find_func(point1, point2):
    if point1[0] == point2[0]:
        return 0, 0
    else:
        a = (point1[1] - point2[1]) / (point1[0] - point2[0])
        b = point1[1] - a * point1[0]
        return a, b

def rotate_integral(tmp, start, end):
    a, b = tmp[0], tmp[1]
    value = (a ** 2 * (end ** 3 - start ** 3) / 3
             + a * b * (end ** 2 - start ** 2)
             + b ** 2 * (end - start))
    return value * pi

def solve(points):
    points.sort()
    point1, point2, point3 = points
    tmp1 = find_func(point1, point2)
    tmp2 = find_func(point2, point3)
    tmp3 = find_func(point1, point3)
    answer = (rotate_integral(tmp3, point1[0], point3[0])
              - rotate_integral(tmp1, point1[0],point2[0])
              - rotate_integral(tmp2, point2[0], point3[0]))
    return abs(answer)

x1, y1, x2, y2, x3, y3 = map(int, input().split())
points1 = [[x1, y1], [x2, y2], [x3, y3]]
points2 = [[y1, x1], [y2, x2], [y3, x3]]
print(solve(points1), end=' ')
print(solve(points2))
