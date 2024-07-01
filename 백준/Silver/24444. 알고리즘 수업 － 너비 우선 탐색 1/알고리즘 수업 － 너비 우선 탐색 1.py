from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

q = deque([r])
order = 0
visited = [0] * (n + 1)
while q:
    now = q.popleft()
    if not visited[now]:
        order += 1
        visited[now] = order
        tmp = [i for i in graph[now] if not visited[i]]
        q += sorted(tmp)
print(*visited[1:], sep='\n')
