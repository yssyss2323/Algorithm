import heapq
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
num_item = list(map(int, input().split()))

arr = [[] for _ in range(n + 1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    arr[a].append((b, l))
    arr[b].append((a, l))

def dijkstra(idx):
    dist = [float('inf') for _ in range(n + 1)]
    dist[idx] = 0
    q = [(0, idx)]
    visited = [False for _ in range(n + 1)]

    while q:
        curr = heapq.heappop(q)
        if visited[curr[1]]:
            continue
        visited[curr[1]] = True
        for x in arr[curr[1]]:
            if dist[x[0]] > dist[curr[1]] + x[1]:
                dist[x[0]] = dist[curr[1]] + x[1]
                heapq.heappush(q, (dist[x[0]], x[0]))
    return dist

ans = 0
for i in range(1, n + 1):
    tmp = 0
    my_dist = dijkstra(i)
    for j in range(1, n + 1):
        if my_dist[j] <= m:
            tmp += num_item[j - 1]
    if ans < tmp:
        ans = tmp
print(ans)