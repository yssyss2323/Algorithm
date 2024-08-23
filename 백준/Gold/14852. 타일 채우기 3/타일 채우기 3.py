n = int(input())
mod = 1000000007
dp = [1, 2]
tmp = dp[0] * 2
for i in range(2, n + 1):
    tmp += dp[1] * 2
    dp = [dp[1], (dp[0] + tmp) % mod]
print(dp[1])