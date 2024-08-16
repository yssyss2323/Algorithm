n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [-1 for _ in range(n + 1)]
visited[1] = 0
stack = [1]
while stack:
    curr = stack.pop()
    for node in graph[curr]:
        if visited[node] == -1:
            stack.append(node)
            visited[node]= curr
print(*visited[2:], sep='\n')