from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
table = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    table[a-1].append(b-1)
    table[b-1].append(a-1)
visited = [0] * n
q = deque([0])
visited[0] = 1
while q:
    curr = q.popleft()
    d = visited[curr]
    nex = table[curr]
    for num in nex:
        if not visited[num]:
            q.append(num)
            visited[num] = d + 1
ans2 = max(visited)
ans1 = visited.index(ans2) + 1
ans3 = visited.count(ans2)
print(ans1, ans2 - 1, ans3)