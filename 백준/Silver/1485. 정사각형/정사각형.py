def len_square(point1, point2):
    return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2

def check_orth(point1, point2, point3):
    return (point1[0] - point2[0]) * (point1[0] - point3[0]) == - (point1[1] - point2[1]) * (point1[1] - point3[1])

def check(point1, point2, point3, point4):
    lengths = [(len_square(point1, point2), point2),
               (len_square(point1, point3), point3),
               (len_square(point1, point4), point4)]
    lengths.sort()
    if lengths[0][0] == lengths[1][0] and len_square(lengths[2][1], lengths[0][1]) == len_square(lengths[2][1], lengths[1][1]):
        if check_orth(point1, lengths[0][1], lengths[1][1]):
            return True
    return False


import sys
input = sys.stdin.readline

for _ in range(int(input())):
    points = []
    for _ in range(4):
        points.append(list(map(int, input().split())))
    if check(*points):
        print(1)
    else:
        print(0)