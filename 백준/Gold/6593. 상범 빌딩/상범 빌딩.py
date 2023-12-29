import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    visited = [[[False for _ in range(c)] for _ in range(r)] for _ in range(l)]
    field = [[[] for _ in range(r)] for _ in range(l)]
    for i in range(l):
        for j in range(r + 1):
            tmp = list(input())
            if tmp: # 입력이 빈 행이 아닌 경우
                field[i][j] += tmp
            if 'S' in tmp: # 출발지점 좌표
                k = tmp.index('S')
                start = [i, j, k, 0] # 좌표와 함께 이동시간을 저장
                field[i][j][k] = '.'
                visited[i][j][k] = True
            if 'E' in tmp: # 도착지점 좌표
                k = tmp.index('E')
                goal = [i, j, k]
                field[i][j][k] = '.'

    # bfs 수행 : 3차원 방향 탐색
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    q = deque()
    q.append(start)
    while q:
        x, y, z, t = q.popleft() # x,y,z 좌표와 t 이동시간
        if [x, y, z] == goal:
            print(f"Escaped in {t} minute(s).")
            break
        for i in range(6):
            nx, ny, nz, nt = x + dx[i], y + dy[i], z + dz[i], t + 1
            if 0 <= nx < l and 0 <= ny < r and 0 <= nz < c and field[nx][ny][nz] == '.' and not visited[nx][ny][nz]:
                q.append([nx, ny, nz, nt])
                visited[nx][ny][nz] = True
    else:
        print("Trapped!")