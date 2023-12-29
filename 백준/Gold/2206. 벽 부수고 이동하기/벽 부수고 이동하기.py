import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
visited = [[0 for _ in range(m)] for _ in range(n)]
# 방문 안했으면 0, 벽 부수고 방문했으면 1, 벽 안부수고 방문했으면 2
field = []
for _ in range(n):
    field.append(list(input()))

visited[0][0] = 2
q = deque()
q.append([0, 0, False, 1])  # x좌표,y좌표,벽부쉈는지 여부,이동길이

# bfs 수행
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while q:
    x, y, breaked, t = q.popleft()
    if x == n - 1 and y == m - 1:  # 목표지점 도달
        print(t)
        break
    for i in range(4):
        nx, ny, nt = x + dx[i], y + dy[i], t + 1
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny]:
                # 방문하지 않은 곳 -> 벽인데 더이상 부실수 없는 경우가 아니면 방문가치 있음
                if not (field[nx][ny] == '1' and breaked):
                    visited[nx][ny] = 1 if breaked else 2
                    nowbreaked = True if (breaked or field[nx][ny] == '1') else False
                    q.append([nx, ny, nowbreaked, nt])
            elif visited[nx][ny] == 1:
                # 한번 부순 이후에 방문한곳 -> 벽이 아니고 아직 안부신 경우에만 방문가치 있음
                if field[nx][ny] == '0' and not breaked:
                    visited[nx][ny] = 2
                    q.append([nx, ny, breaked, nt])
else:
    print(-1)
