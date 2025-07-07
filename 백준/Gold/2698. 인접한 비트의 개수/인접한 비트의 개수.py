import sys
input = sys.stdin.readline

maximum = 100

dp = [[[0, 0] for _ in range(maximum + 1)] for _ in range(maximum + 1)]
dp[1][0][0] = 1
dp[1][0][1] = 1
for n in range(2, maximum + 1):
    for k in range(n):
        if k == 0:
            dp[n][k][0] = dp[n - 1][0][0] + dp[n - 1][0][1]
            dp[n][k][1] = dp[n - 1][0][0]
        else:
            dp[n][k][0] = dp[n - 1][k][0] + dp[n - 1][k][1]
            dp[n][k][1] = dp[n - 1][k][0] + dp[n - 1][k - 1][1]

for _ in range(int(input())):
    n, k = map(int, input().split())
    print(dp[n][k][0] + dp[n][k][1])
