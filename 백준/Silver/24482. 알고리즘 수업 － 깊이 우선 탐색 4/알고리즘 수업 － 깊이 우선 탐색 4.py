import sys
input = sys.stdin.readline

n,m,r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(1, m + 1):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

stack = [(r, 0)]
visited = [-1] * (n + 1)
while stack:
    current, depth = stack.pop()
    if visited[current] == -1:
        visited[current] = depth
    tmp = [(node, depth + 1) for node in graph[current] if visited[node] == -1]
    tmp.sort()
    stack += tmp
print(*visited[1:],sep='\n')