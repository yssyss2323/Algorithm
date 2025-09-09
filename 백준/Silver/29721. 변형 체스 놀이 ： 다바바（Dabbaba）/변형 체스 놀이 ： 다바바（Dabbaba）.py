import sys
input = sys.stdin.readline

n, k = map(int, input().split())
pos = [tuple(map(int, input().split())) for _ in range(k)]

check = set(pos)
dx,dy = [2, -2, 0, 0], [0, 0, 2, -2]

ans = 0
for x, y in pos:
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 1 or nx > n or ny < 1 or ny > n:
            continue
        if (nx, ny) not in check:
            check.add((nx, ny))
            ans += 1
print(ans)