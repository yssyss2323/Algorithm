n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = 0
for i in range(1, n - 1):
    for j in range(1, m - 1):
        curr = arr[i][j] - 1
        for k in range(4):
            curr = min(curr, arr[i + dx[k]][j + dy[k]])
        ans += max(curr, 0)
print(ans)