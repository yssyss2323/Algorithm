x1, y1, z1, x2, y2, z2 = map(int, input().split())
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
n = int(input())

lines = list(map(int, input().split()))
lines.append(distance)
if sum(lines) - max(lines) * 2 >= 0:
    print('YES')
else:
    print('NO')