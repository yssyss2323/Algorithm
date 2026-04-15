from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

good_tomato = []
bad_tomato_cnt = 0

m, n, h = map(int, input().split())
box = [[[-1] * m for _ in range(n)] for _ in range(h)]
for i in range(h):
    for j in range(n):
        curr = list(map(int, input().split()))
        for k in range(m):
            if curr[k] == 1:
                box[i][j][k] = curr[k]
                good_tomato.append((i, j, k, 0))
            elif curr[k] == 0:
                box[i][j][k] = curr[k]
                bad_tomato_cnt += 1

q = deque(good_tomato)
required_day = 0
while q:
    curr_x, curr_y, curr_z, curr_d = q.popleft()
    if curr_d > required_day:
        required_day = curr_d

    for i in range(6):
        nx = curr_x + dx[i]
        ny = curr_y + dy[i]
        nz = curr_z + dz[i]
        nd = curr_d + 1

        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and box[nx][ny][nz] == 0:
            q.append((nx, ny, nz, nd))
            box[nx][ny][nz] = 1
            bad_tomato_cnt -= 1

if bad_tomato_cnt:
    print(-1)
else:
    print(required_day)