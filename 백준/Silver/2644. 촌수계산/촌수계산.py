from collections import deque

n = int(input())
person1, person2 = map(int, input().split())
graph = [[] for _ in range(n + 1)]
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n + 1)
visited[person1] = True
q = deque([(person1, 0)])
while q:
    now, distance = q.popleft()
    if now == person2:
        print(distance)
        break
    for i in graph[now]:
        if not visited[i]:
            visited[i] = True
            q.append((i,distance + 1))
else:
    print(-1)