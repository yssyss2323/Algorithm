import sys
input = lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())
board = []
points = []
zeros = []
for i in range(n):
    tmp = list(map(int, input()))
    for j in range(m):
        if tmp[j] == 1:
            tmp[j] = -1
            points.append((i, j))
        else:
            zeros.append((i, j))
    board.append(tmp)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

check = [-1]
visited = set()
id = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            id += 1
            board[i][j] = id
            stack = [(i, j)]
            cnt = 1
            while stack:
                cx, cy = stack.pop()
                for k in range(4):
                    nx, ny = cx + dx[k], cy + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                        stack.append((nx, ny))
                        board[nx][ny] = id
                        cnt += 1
            check.append(cnt)

ans = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == -1:
            cnt = 1
            visited = set()
            for k in range(4):
                ni, nj = i + dx[k], j + dy[k]
                if 0 <= ni < n and 0 <= nj < m and board[ni][nj] != -1:
                    if board[ni][nj] not in visited:
                        cnt += check[board[ni][nj]]
                        visited.add(board[ni][nj])
            ans[i][j] = cnt % 10

for x in ans:
    print(*x, sep='')
