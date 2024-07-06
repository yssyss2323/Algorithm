def find_grad(pnt1, pnt2):
    return pnt1[1] - pnt2[1], -pnt1[0] + pnt2[0]

def find_line(grad, pnt):
    return -grad[1], grad[0], grad[1] * pnt[0] - grad[0] * pnt[1]

def find_pnt(line1, line2):
    if line1[1] * line2[2] - line1[2] * line2[1]:
        x = (line1[1] * line2[2] - line1[2] * line2[1]) / (line1[0] * line2[1] - line1[1] * line2[0])
    else:
        x = 0
    if line1[0] * line2[2] - line1[2] * line2[0]:
        y = (line1[0] * line2[2] - line1[2] * line2[0]) / (line1[1] * line2[0] - line1[0] * line2[1])
    else:
        y = 0
    return (x, y)


import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    point1 = tuple(map(float, input().split()))
    point2 = tuple(map(float, input().split()))
    point3 = tuple(map(float, input().split()))
    line1 = find_line(find_grad(point1, point2), point3)
    line2 = find_line(find_grad(point2, point3), point1)
    point = find_pnt(line1, line2)
    print(f"{point[0]:.4f} {point[1]:.4f}")
