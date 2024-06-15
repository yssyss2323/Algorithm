n = int(input())
dp = [1, 3]
if n <= 2:
    print(dp[n - 1])
else:
    dp += [0] * (n - 2)
    for i in range(2, n):
        dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 10007
    print(dp[n - 1])
