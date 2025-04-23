import sys
input = sys.stdin.readline

n = int(input())
size = [0] * (n + 1)
size[:2] = map(int, input().split())
for i in range(2, n + 1):
    _, x = map(int, input().split())
    size[i] = x

dp = [[0] * n for _ in range(n)]
for d in range(2, n + 1):
    for i in range(n - d + 1):
        j = i + d - 1
        dp[i][j] = float('inf')
        for k in range(i, j):
            tmp = dp[i][k] + dp[k + 1][j] + size[i] * size[k + 1] * size[j + 1]
            if dp[i][j] > tmp:
                dp[i][j] = tmp

print(dp[0][-1])
