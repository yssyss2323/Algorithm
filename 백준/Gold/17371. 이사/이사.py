import sys
input = sys.stdin.readline

def distance_square(point1, point2):
    return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2

n = int(input())
points = []
for _ in range(n):
    points.append(list(map(int, input().split())))

maximums = [0] * n
for i in range(n):
    for j in range(n):
        tmp = distance_square(points[i], points[j])
        if tmp > maximums[i]:
            maximums[i] = tmp
target = min(maximums)
idx = maximums.index(target)
print(*points[idx])