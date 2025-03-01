import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    arr[s].append([e, c])
start, end = map(int, input().split())

dist = [[float('inf'), [start]] for _ in range(n + 1)]
dist[start][0] = 0

q = [(0, start)]
visited = [False for _ in range(n + 1)]

while q:
    curr = heapq.heappop(q)
    if visited[curr[1]]:
        continue
    visited[curr[1]] = True
    for x in arr[curr[1]]:
        if dist[x[0]][0] > dist[curr[1]][0] + x[1]:
            dist[x[0]][0] = dist[curr[1]][0] + x[1]
            dist[x[0]][1] = dist[curr[1]][1] +[x[0]]
            heapq.heappush(q, (dist[x[0]], x[0]))

print(dist[end][0])
print(len(dist[end][1]))
print(*dist[end][1])