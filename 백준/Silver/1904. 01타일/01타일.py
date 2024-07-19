n = int(input())

dp = [0, 1]
for _ in range(n):
    dp[0], dp[1] = dp[1], (dp[0] + dp[1]) % 15746
print(dp[-1])