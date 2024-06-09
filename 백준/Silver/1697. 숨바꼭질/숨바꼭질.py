from collections import deque

def bfs(n, k, visited):
    q = deque([[n, 0]])
    while q:
        now = q.popleft()
        if now[0] == k:
            return now[1]
        next = [now[0] * 2, now[0] + 1, now[0] - 1]
        for i in range(3):
            if 0 <= next[i] <= 10 ** 5 and not visited[next[i]]:
                q.append([next[i], now[1] + 1])
                visited[next[i]] = True


N, K = map(int, input().split())
visited = [False] * (10 ** 5 + 1)
print(bfs(N, K, visited))
