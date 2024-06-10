from collections import deque

def bfs(n, k, visited):
    q = deque([[n, [n]]])
    while q:
        now = q.popleft()
        if now[0] == k:
            return now[1]
        next = [now[0] * 2, now[0] + 1, now[0] - 1]
        for i in range(3):
            if 0 <= next[i] <= 10 ** 5 and not visited[next[i]]:
                q.append([next[i], now[1] + [next[i]]])
                visited[next[i]] = True


N, K = map(int, input().split())
if N >= K:
    print(N - K)
    print(*list(range(N, K - 1, -1)))
else:
    visited = [False] * (10 ** 5 + 1)
    answer = bfs(N, K, visited)
    print(len(answer) - 1)
    print(*answer)
