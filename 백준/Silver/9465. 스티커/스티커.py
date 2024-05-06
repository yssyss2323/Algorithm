import sys
input = lambda:sys.stdin.readline().rstrip()

Testcase = int(input())
for _ in range(Testcase):
    n = int(input())
    stickers = []
    for _ in range(2):
        stickers.append(list(map(int,input().split())))

    dp = [[0,stickers[0][0]], [0, stickers[1][0]]]

    for i in range(1, n):
        tmp1 = max(dp[1][0] + stickers[0][i], dp[1][1] + stickers[0][i])
        tmp2 = max(dp[0][1] + stickers[1][i], dp[0][0] + stickers[1][i])
        dp[0] = [dp[0][1], tmp1]
        dp[1] = [dp[1][1], tmp2]

    print(max(dp[0][1], dp[1][1]))
