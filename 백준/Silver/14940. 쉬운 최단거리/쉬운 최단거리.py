from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

def bfs(graph, a, b):
    row, col = len(graph), len(graph[0])
    ans = [[-1] * col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            if graph[i][j] in [0, 2]:
                ans[i][j] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque([[a, b, 0]])
    while q:
        now = q.popleft()
        for i in range(4):
            next = [now[0] + dx[i], now[1] + dy[i], now[2] + 1]
            if 0 <= next[0] < row and 0 <= next[1] < col and graph[next[0]][next[1]] == 1:
                if ans[next[0]][next[1]] == -1:
                    ans[next[0]][next[1]] = next[2]  # 방문처리
                    q.append(next)
    return ans


n, m = map(int, input().split())
ground = []
for i in range(n):
    tmp = list(map(int, input().split()))
    if 2 in tmp:
        target = [i, tmp.index(2)]
    ground.append(tmp)

answer = bfs(ground, *target)
for i in range(n):
    print(*answer[i])
