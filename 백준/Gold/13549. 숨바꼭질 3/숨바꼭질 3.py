from collections import deque

def bfs(n, k, visited):
    q = deque([[n, 0]])
    while q:
        now = q.popleft()
        check = now[0]
        if check == k:
            return now[1]
        while True:
            check *= 2
            if check <= 10 ** 5 and not visited[check]:
                visited[check] = True
                q.append([check, now[1]])
            else:
                break
        next = [now[0] - 1, now[0] + 1]
        for i in range(2):
            if 0 <= next[i] <= 10 ** 5 and not visited[next[i]]:
                q.append([next[i], now[1] + 1])
                visited[next[i]] = True


N, K = map(int, input().split())
visited = [False] * (10 ** 5 + 1)
print(bfs(N, K, visited))
