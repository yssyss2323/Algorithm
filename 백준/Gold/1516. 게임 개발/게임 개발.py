from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
time = [0 for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    tmp = list(map(int, input().split()))
    t, tmp = tmp[0], tmp[1:-1]
    time[i] = t
    for j in tmp:
        graph[j].append(i)
        indegree[i] += 1

q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

ans = [0 for _ in range(n + 1)]
while q:
    curr = q.popleft()
    tmp = graph[curr]
    tt = time[curr]
    for node in tmp:
        ans[node] = max(ans[node], ans[curr] + tt)
        indegree[node] -= 1
        if indegree[node] == 0:
            q.append(node)

for i in range(1, n + 1):
    print(ans[i] + time[i])
