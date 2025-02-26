n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]

dp[0][1][0] = 1
for i in range(2, n):
    if house[0][i] != 1:
        dp[0][i][0] = dp[0][i - 1][0]

for i in range(1, n):
    for j in range(1, n):
        if house[i][j] != 1:
            dp[i][j][0] += dp[i][j - 1][0] + dp[i][j - 1][1]
            dp[i][j][2] = dp[i - 1][j][1] + dp[i - 1][j][2]
            if house[i - 1][j] != 1 and house[i][j - 1] != 1:
                dp[i][j][1] = sum(dp[i - 1][j - 1])
print(sum(dp[-1][-1]))