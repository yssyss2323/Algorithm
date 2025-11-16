from collections import deque
import sys
input = sys.stdin.readline

def is_connected(point1, point2):
    return abs(point1[0] - point2[0]) <= 2 and abs(point1[1] - point2[1]) <= 2

n, t = map(int, input().split())
points = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]
points.sort(key=lambda x:x[1])

check_dict = {points[i]:i for i in range(n + 1)}
check = set(points)
matrix = [[] for _ in range(n + 1)]
near_range = [-2, -1, 0, 1, 2]
for i in range(n + 1):
    curr_point = points[i]
    near_points = []
    for j in near_range:
        for k in near_range:
            if j == 0 and k == 0:
                continue
            near_points.append((curr_point[0] + j, curr_point[1] + k))
    for point in near_points:
        if point in check:
            matrix[i].append(check_dict[point])

q = deque([(0, 0)])
visited = [True] + [False] * n
while q:
    curr, cnt = q.popleft()
    if points[curr][1] == t:
        print(cnt)
        break
    for cand in matrix[curr]:
        if not visited[cand]:
            q.append((cand, cnt + 1))
            visited[cand] = True
else:
    print(-1)