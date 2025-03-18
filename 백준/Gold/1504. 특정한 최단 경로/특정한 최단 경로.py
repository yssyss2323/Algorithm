import heapq
import sys
input = sys.stdin.readline

n, e = map(int, input().split())

arr = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))
v1, v2 = map(int, input().split())

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

ans = min(
    dijkstra(1)[v1] + dijkstra(v1)[v2] + dijkstra(v2)[n],
    dijkstra(1)[v2] + dijkstra(v2)[v1] + dijkstra(v1)[n]
)

print(ans if ans != float('inf') else -1)