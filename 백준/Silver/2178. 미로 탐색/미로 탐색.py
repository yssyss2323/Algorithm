from collections import deque
import sys
input = lambda: sys.stdin.readline().rstrip()

def bfs(graph):
    n, m = len(graph), len(graph[0])
    visited = [[0] * m for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque([[0, 0]])
    visited[0][0] = 1
    while q:
        now = q.popleft()
        if now == [n - 1, m - 1]:
            return visited[n - 1][m - 1]
        for i in range(4):
            xnext = now[0] + dx[i]
            ynext = now[1] + dy[i]
            if 0 <= xnext < n and 0 <= ynext < m and graph[xnext][ynext] == '1':
                if not visited[xnext][ynext]:
                    q.append([xnext, ynext])
                    visited[xnext][ynext] = visited[now[0]][now[1]] + 1


N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(input())

print(bfs(maze))
