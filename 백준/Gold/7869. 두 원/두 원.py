from math import pi, acos

def cosine(a, b, c):
    return (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)

def square_distance(point1, point2):
    return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2


x1, y1, r1, x2, y2, r2 = map(float, input().split())
if r1 >= r2:
    A, B = [x1, y1, r1], [x2, y2, r2]
else:
    A, B = [x2, y2, r2], [x1, y1, r1]

answer = 0
stand_value = square_distance(A, B)
if stand_value >= (r1 + r2) ** 2:
    answer = 0
elif stand_value <= (r1 - r2) ** 2:
    answer = pi * B[2] ** 2
else:
    cos_A = cosine(A[2], stand_value ** 0.5, B[2])
    part1 = acos(cos_A) * A[2] ** 2 - A[2] ** 2 * cos_A * (1 - cos_A ** 2) ** 0.5
    cos_B = cosine(B[2], stand_value ** 0.5, A[2])
    part2 = acos(cos_B) * B[2] ** 2 - B[2] ** 2 * cos_B * (1 - cos_B ** 2) ** 0.5
    answer = part1 + part2
print("%.3f" % answer)
