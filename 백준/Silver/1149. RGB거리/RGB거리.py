n = int(input())
rgb_cost = []
for _ in range(n):
    rgb_cost.append(list(map(int, input().split())))
dp = [[0] * 3 for _ in range(n)]
dp[0] = rgb_cost[0]
for i in range(1, n):
    for j in range(3):
        dp[i][j] = min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3]) + rgb_cost[i][j]
print(min(dp[n - 1]))