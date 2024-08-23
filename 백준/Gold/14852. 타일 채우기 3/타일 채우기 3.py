n = int(input())
mod = 1000000007
dp = [1] * (n + 1)
dp[1] = 2
tmp = dp[0] * 2
for i in range(2, n + 1):
    tmp += dp[i - 1] * 2
    dp[i] = (dp[i - 2] + tmp) % mod
print(dp[n])