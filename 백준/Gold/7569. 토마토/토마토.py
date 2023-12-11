from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()
M, N, H = map(int, input().split())
# 맵 초기화
field = [[[-1] * (M + 2)] * (N + 2)]
for _ in range(H):
    tmp = [[-1] * (M + 2)]
    for _ in range(N):
        tmp.append([-1] + list(map(int, input().split())) + [-1])
    tmp += [[-1] * (M + 2)]
    field.append(tmp)
field.append([[-1] * (M + 2)] * (N + 2))
# 익은 토마토 (큐)
welldone = deque()
for i in range(H + 2):
    for j in range(N + 2):
        for k in range(M + 2):
            if field[i][j][k] == 1:
                welldone.append([i, j, k, 0])

# 이동방향
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
# bfs 수행
day = 0
while welldone:
    x, y, z, d = welldone.popleft()
    for i in range(6):
        newx, newy, newz = x + dx[i], y + dy[i], z + dz[i]
        if field[newx][newy][newz] == 0:
            welldone.append([newx, newy, newz, d + 1])
            field[newx][newy][newz] = 1
            day = d + 1
# 정답 출력
for height in field:
    for row in height:
        if 0 in row:
            print(-1)
            exit()
print(day)
