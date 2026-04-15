from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

good_tomato = []
bad_tomato_cnt = 0

m, n, h = map(int, input().split())
box = [[[-1] * (m + 2) for _ in range(n + 2)] for _ in range(h + 2)] # -1로 래핑
for i in range(1, h + 1):
    for j in range(1, n + 1):
        curr = list(map(int, input().split()))
        for k in range(1, m + 1):
            if curr[k - 1] == 1:
                box[i][j][k] = curr[k - 1]
                good_tomato.append((i, j, k, 0))
            elif curr[k - 1] == 0:
                box[i][j][k] = curr[k - 1]
                bad_tomato_cnt += 1

q = deque(good_tomato)
required_day = 0
while q:
    curr_x, curr_y, curr_z, curr_d = q.popleft()

    for i in range(6):
        nx = curr_x + dx[i]
        ny = curr_y + dy[i]
        nz = curr_z + dz[i]
        nd = curr_d + 1

        if box[nx][ny][nz] == 0:
            q.append((nx, ny, nz, nd))
            box[nx][ny][nz] = 1
            bad_tomato_cnt -= 1
            required_day = curr_d + 1

if bad_tomato_cnt:
    print(-1)
else:
    print(required_day)