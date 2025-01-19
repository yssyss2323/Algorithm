import heapq
import sys
input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
rev_graph = [[] for _ in range(n + 1)]
dist = [float('inf') for _ in range(n + 1)]
dist[x] = 0
for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append([e, t])
    rev_graph[e].append([s, t])

visited = [False for _ in range(n + 1)]
q = [[dist[x], x]]
while q:
    curr = heapq.heappop(q)
    if not visited[curr[1]]:
        visited[curr[1]] = True
        for node in graph[curr[1]]:
            if dist[node[0]] > curr[0] + node[1]:
                dist[node[0]] = curr[0] + node[1]
                heapq.heappush(q, [dist[node[0]], node[0]])

rev_dist = [float('inf') for _ in range(n + 1)]
rev_dist[x] = 0
visited = [False for _ in range(n + 1)]
q = [[rev_dist[x], x]]
while q:
    curr = heapq.heappop(q)
    if not visited[curr[1]]:
        visited[curr[1]] = True
        for node in rev_graph[curr[1]]:
            if rev_dist[node[0]] > curr[0] + node[1]:
                rev_dist[node[0]] = curr[0] + node[1]
                heapq.heappush(q, [rev_dist[node[0]], node[0]])

print(max([dist[i] + rev_dist[i] for i in range(1, n + 1)]))