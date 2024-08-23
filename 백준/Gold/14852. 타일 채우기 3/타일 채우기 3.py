n = int(input())
if n == 1:
    print(2)
else:
    mod = 1000000007
    dp = [1] * (n + 1)
    dp[1] = 2
    dp[2] = 7
    tmp = 0
    for i in range(3, n + 1):
        tmp += dp[i - 3]
        dp[i] = (2 * dp[i - 1] + 3 * dp[i - 2] + 2 * tmp) % mod
    print(dp[n])