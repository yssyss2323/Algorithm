from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
relations = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)

visited = [False for _ in range(n + 1)]
q = deque([(1, 0)])
visited[1] = True

cnt = -1
while q:
    curr, dist = q.popleft()
    if dist > 2:
        break
    cnt += 1
    for friend in relations[curr]:
        if not visited[friend]:
            visited[friend] = True
            q.append((friend, dist + 1))
print(cnt)