import sys
input = sys.stdin.readline

def dist(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

tot = 0
for i in range(n - 1):
    point1 = points[i]
    for j in range(i + 1, n):
        point2 = points[j]
        tot += dist(point1, point2)

ans = tot * 2 / n
print(ans)