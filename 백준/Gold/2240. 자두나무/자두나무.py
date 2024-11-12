import sys
input = sys.stdin.readline

t, w = map(int, input().split())
arr = [int(input()) for _ in range(t)]

dp = [[0] * (w + 1) for _ in range(t + 1)]

for i in range(1, t + 1):
    dp[i][0] = dp[i - 1][0] + (arr[i - 1] % 2) * 1
    for j in range(1, w + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])
        if j % 2 != arr[i - 1] % 2:
            dp[i][j] += 1
print(max(dp[t]))