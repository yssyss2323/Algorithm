MOD = 1000000009

test = [int(input()) for _ in range(int(input()))]
n = max(test)
if n <= 3:
    dp = [0, 1, 1, 3]
    for t in test:
        print(dp[t])
else:
    dp = [[0,0,0] for _ in range(n + 1)]
    dp[1] = [1,0,0]
    dp[2] = [0,1,0]
    dp[3] = [1,1,1]
    for i in range(4, n + 1):
        for k in range(1, 4):
            dp[i][k - 1] = (sum(dp[i - k]) - dp[i - k][k - 1]) % MOD
    for t in test:
        print(sum(dp[t]) % MOD)