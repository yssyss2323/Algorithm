from math import tan, atan, cos

h, v = map(float, input().split())

angle = atan(v / h) / 2
x = v - h * tan(angle)

h2 = h / cos(angle) / 2
v2 = x * cos(angle)

print('%.2f %.2f' % (h2, v2))
