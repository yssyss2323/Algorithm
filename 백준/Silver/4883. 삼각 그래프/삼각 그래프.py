import sys
input = sys.stdin.readline

t = 1
while True:
    n = int(input())
    if n == 0:
        break
    cost = [tuple(map(int,input().split())) for _ in range(n)]

    dp = [[0,0,0] for _ in range(n)]
    dp[0] = [cost[0][1], cost[0][1], cost[0][1] + cost[0][2]]
    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][0]
        dp[i][1] = min(dp[i][0], dp[i - 1][0], dp[i - 1][1], dp[i - 1][2]) + cost[i][1]
        dp[i][2] = min(dp[i][1], dp[i - 1][1], dp[i - 1][2]) + cost[i][2]
    print(f"{t}. {dp[n - 1][1]}")
    t += 1