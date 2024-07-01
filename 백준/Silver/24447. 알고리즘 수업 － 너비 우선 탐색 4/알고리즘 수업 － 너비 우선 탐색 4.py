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
order = 0
visited = [False] * (n + 1)
anslist = [0] * (n + 1)
while q:
    now, depth = q.popleft()
    if not visited[now]:
        order += 1
        visited[now] = True
        anslist[now] = order * depth
        tmp = [(i, depth + 1) for i in graph[now] if not visited[i]]
        q += tmp
print(sum(anslist[1:]))
