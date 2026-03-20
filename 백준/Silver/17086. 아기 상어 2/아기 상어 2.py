from collections import deque

dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

def dfs(graph, start, visited):
    visited.add((start[0], start[1]))
    q = deque([start])
    while q:
        x, y, d = q.popleft()
        if graph[x][y] == 1:
            return d
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            nd = d + 1
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny, nd))


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            curr = dfs(board, (i, j, 0), set())
            ans = max(ans, curr)
print(ans)