n, k = map(int, input().split())
mod = 10 ** 9

dp = [[0] * (n + 1) for _ in range(k + 1)]
dp[1] = [1] * (n + 1)
for i in range(2, k + 1):
    for j in range(n + 1):
        for t in range(j + 1):
            dp[i][j] += dp[i - 1][t] % mod
print(dp[k][n] % mod)