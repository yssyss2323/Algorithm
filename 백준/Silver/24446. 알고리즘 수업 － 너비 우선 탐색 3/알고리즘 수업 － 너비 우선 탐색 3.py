from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

q = deque([(r, 0)])
visited = [-1] * (n + 1)
while q:
    now, depth = q.popleft()
    if visited[now] == -1:
        visited[now] = depth
        tmp = [(i, depth + 1) for i in graph[now] if visited[i] == -1]
        q += tmp
print(*visited[1:], sep='\n')
