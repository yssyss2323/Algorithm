n = int(input())
MOD = 10 ** 9 + 9

if n == 1:
    print(0)
else:
    dp = [2, 2, 2]
    for i in range(2, n):
        dp = [(dp[0] + dp[1] + dp[2]) % MOD,
              (dp[0] + dp[1] + dp[2]) % MOD,
              (dp[0] + dp[1] + dp[2]) % MOD]
    print(dp[0])