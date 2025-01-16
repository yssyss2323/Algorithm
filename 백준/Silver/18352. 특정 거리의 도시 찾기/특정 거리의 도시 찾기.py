from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
arr = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)

q = deque([x])
visited = [-1 for _ in range(n + 1)]
visited[x] = 0
while q:
    curr = q.popleft()
    nex = arr[curr]
    for p in nex:
        if visited[p] == -1:
            visited[p] = visited[curr] + 1
            q.append(p)

anslist = [i for i in range(1, n + 1) if visited[i] == k]
if anslist:
    for ans in anslist:
        print(ans)
else:
    print(-1)