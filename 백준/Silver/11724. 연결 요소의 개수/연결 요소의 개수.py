import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
visited = [False] * N

for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

ans = 0
stack = []
for i in range(N):
    if not visited[i]:
        visited[i] = True
        ans += 1
        for j in graph[i]:
            if not visited[j]:
                visited[j] = True
                stack.append(j)
            while stack:
                now = stack.pop()
                for tmp in graph[now]:
                    if not visited[tmp]:
                        visited[tmp] = True
                        stack.append(tmp)
print(ans)
