from math import acos, pi
import sys
input = sys.stdin.readline

n = int(input())
max_length = 0
max_points = []
for _ in range(n):
    x,y = map(int,input().split())
    length_square = x**2 + y**2
    if length_square > max_length:
        max_length = length_square
        max_points = [(x,y)]
    elif length_square == max_length:
        max_points.append((x,y))
max_points.append(max_points[0])

angle = 0
num_points = len(max_points)
if num_points == 2:
    print(360)
else:
    for i in range(num_points - 1):
        pointa, pointb = max_points[i], max_points[i+1]
        x1,y1 = pointa
        x2,y2 = pointb
        cos_val = (x1**2 + y1**2 + x2**2 + y2**2 - (x1-x2)**2 - (y1-y2)**2)\
                    /(2*(x1**2 + y1**2)**0.5 * (x2**2 + y2**2)**0.5)
        cos_val = max(-1, min(1, cos_val))
        tmp_angle = acos(cos_val) * 180 / pi
        if x1 * y2 - x2 * y1 < 0:
            tmp_angle = 360 - tmp_angle
        if tmp_angle > angle:
            angle = tmp_angle
    print(angle)