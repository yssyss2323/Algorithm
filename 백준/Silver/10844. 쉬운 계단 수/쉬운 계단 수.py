length = int(input())
dp = [0] + [1] * 9
MOD = 10 ** 9
for _ in range(length - 1):
    dp = [dp[1] % MOD,
          (dp[0] + dp[2]) % MOD,
          (dp[1] + dp[3]) % MOD,
          (dp[2] + dp[4]) % MOD,
          (dp[3] + dp[5]) % MOD,
          (dp[4] + dp[6]) % MOD,
          (dp[5] + dp[7]) % MOD,
          (dp[6] + dp[8]) % MOD,
          (dp[7] + dp[9]) % MOD,
          dp[8] % MOD]
print(sum(dp) % MOD)