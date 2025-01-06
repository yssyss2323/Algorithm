import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
arr = [[] for _ in range(v + 1)]
for _ in range(e):
    uu, vv, ww = map(int, input().split())
    arr[uu].append([vv, ww])

dist = [float('inf') for  _ in range(v + 1)]
dist[k] = 0

q = [(0, k)]
visited = [False for _ in range(v + 1)]

while q:
    curr = heapq.heappop(q)
    if visited[curr[1]]:
        continue
    visited[curr[1]] = True
    for x in arr[curr[1]]:
        if dist[x[0]] > dist[curr[1]] + x[1]:
            dist[x[0]] = dist[curr[1]] + x[1]
            heapq.heappush(q, (dist[x[0]], x[0]))

for i in range(1, v + 1):
    if visited[i]:
        print(dist[i])
    else:
        print('INF')