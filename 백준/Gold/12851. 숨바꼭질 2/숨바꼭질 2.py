from collections import deque

def bfs(n, k, visited):
    q = deque([[n, 0]])
    cnt = 0
    time = float('inf')
    while q:
        now = q.popleft()
        visited[now[0]] = True
        if now[1] == time + 1:
            return time, cnt
        if now[0] == k:
            cnt += 1
            time = now[1]
        next = [now[0] * 2, now[0] + 1, now[0] - 1]
        for i in range(3):
            if 0 <= next[i] <= 10 ** 5 and not visited[next[i]]:
                q.append([next[i], now[1] + 1])


N, K = map(int, input().split())
if N >= K:
    print(N - K)
    print(1)
else:
    visited = [False] * (10 ** 5 + 1)
    print(*bfs(N, K, visited), sep='\n')
