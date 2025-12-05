n = int(input())
mod = 987654321

dp = [1] * 9
for _ in range(1, n):
    dp = [(dp[0] + dp[1] + dp[2]) % mod,
          (dp[0] + dp[1] + dp[2] + dp[3]) % mod,
          (dp[0] + dp[1] + dp[2] + dp[3] + dp[4]) % mod,
          (dp[1] + dp[2] + dp[3] + dp[4] + dp[5]) % mod,
          (dp[2] + dp[3] + dp[4] + dp[5] + dp[6]) % mod,
          (dp[3] + dp[4] + dp[5] + dp[6] + dp[7]) % mod,
          (dp[4] + dp[5] + dp[6] + dp[7] + dp[8]) % mod,
          (dp[5] + dp[6] + dp[7] + dp[8]) % mod,
          (dp[6] + dp[7] + dp[8]) % mod]
print(sum(dp) % mod)