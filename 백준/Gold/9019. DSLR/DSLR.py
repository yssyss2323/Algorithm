from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    visited = [False] * 10000
    a, b = map(int, input().split())
    q = deque([(a, '')])
    visited[a] = True
    while q:
        now, ans = q.popleft()
        if now == b:
            print(ans)
            break
        nextlist = [
            (now * 2 % 10000, ans + 'D'),
            (now - 1 if now > 0 else 9999, ans + 'S'),
            ((now % 1000) * 10 + now // 1000, ans + 'L'),
            ((now % 10) * 1000 + now // 10, ans + 'R')
        ]
        for i in range(4):
            if not visited[nextlist[i][0]]:
                q.append(nextlist[i])
                visited[nextlist[i][0]] = True
