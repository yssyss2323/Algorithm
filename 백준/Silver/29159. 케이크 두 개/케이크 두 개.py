def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

def find_line(point1, point2):
    if point1[1] == point2[1]:
        p = "0"
        q1 = point1[1] // gcd(point1[1], 4)
        q2 = 4 // gcd(point1[1], 4)
        if q2 == 1:
            q = str(q1)
        else:
            q = str(q1) + "/" + str(q2)
        print(p, q)
    else:
        p1 = point2[1] - point1[1]
        p2 = point2[0] - point1[0]
        q1 = point1[1] * (point2[0] - point1[0]) - point1[0] * (point2[1] - point1[1])
        q2 = (point2[0] - point1[0]) * 4
        pp1 = p1 // gcd(p1, p2)
        pp2 = p2 // gcd(p1, p2)
        qq1 = q1 // gcd(q1, q2)
        qq2 = q2 // gcd(q1, q2)
        if pp2 == 1:
            p = str(pp1)
        else:
            p = str(pp1) + "/" + str(pp2)
        if qq2 == 1:
            q = str(qq1)
        else:
            q = str(qq1) + "/" + str(qq2)
        print(p, q)

first_point = [0, 0]
for _ in range(4):
    x, y = map(int, input().split())
    first_point[0] += x
    first_point[1] += y

second_point = [0, 0]
for _ in range(4):
    x, y = map(int, input().split())
    second_point[0] += x
    second_point[1] += y

find_line(first_point, second_point)