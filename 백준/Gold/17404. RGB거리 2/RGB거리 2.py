import sys
input = sys.stdin.readline

n = int(input())
rgb_cost = [list(map(int, input().split())) for _ in range(n)]

dp = [[0, 0, 0] for _ in range(n)]
ans = float('inf')
for i in range(3):
    dp[0] = [float('inf')] * 3
    dp[0][i] = rgb_cost[0][i]
    for j in range(1, n):
        dp[j][0] = rgb_cost[j][0] + min(dp[j - 1][1], dp[j - 1][2])
        dp[j][1] = rgb_cost[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = rgb_cost[j][2] + min(dp[j - 1][0], dp[j - 1][1])
    dp[n - 1][i] = float('inf')
    tmp = min(dp[n - 1])
    if ans > tmp:
        ans = tmp

print(ans)