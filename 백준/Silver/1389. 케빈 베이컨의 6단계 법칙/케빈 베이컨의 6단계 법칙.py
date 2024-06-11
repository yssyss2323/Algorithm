from collections import deque
import sys
input = sys.stdin.readline
def bfs(graph, start):
    q = deque([start])
    visited = [-1] * N
    visited[start] = 0
    while q:
        now = q.popleft()
        for i in range(N):
            if graph[now][i] and visited[i] == -1:
                q.append(i)
                visited[i] = visited[now] + 1
    return sum(visited)


N, M = map(int, input().split())
relations = [[False] * N for _ in range(N)]
for _ in range(M):
    i, j = map(int, input().split())
    relations[i - 1][j - 1] = True
    relations[j - 1][i - 1] = True

kevin_nums = [[-1] * N for _ in range(N)]
check = float('inf')
for i in range(N):
    if check > bfs(relations, i):
        check = bfs(relations, i)
        answer = i + 1
print(answer)
