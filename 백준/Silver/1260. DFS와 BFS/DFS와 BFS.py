import sys
input = sys.stdin.readline

def dfs(graph, start):
    ans = []
    stack = [start]
    visited = [False] * len(graph)
    while stack:
        now = stack.pop()
        if visited[now]:
            continue
        else:
            visited[now] = True
            ans.append(now)
            for i in range(N, 0, -1):
                if graph[now][i]:
                    stack.append(i)
    return ans

def bfs(graph, start):
    from collections import deque

    ans = []
    q = deque([start])
    visited = [False] * len(graph)
    visited[start] = True
    while q:
        now = q.popleft()
        ans.append(now)
        for i in range(1, N + 1):
            if graph[now][i] and not visited[i]:
                q.append(i)
                #ans.append(i)
                visited[i] = True
    return ans


N, M, V = map(int, input().split())
my_graph = [[None]] + [[None] + [False] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    my_graph[a][b] = True
    my_graph[b][a] = True
print(*dfs(my_graph, V))
print(*bfs(my_graph, V))