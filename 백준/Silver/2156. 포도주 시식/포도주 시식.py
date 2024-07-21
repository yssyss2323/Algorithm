import sys
input = sys.stdin.readline

num_cup = int(input())
drinks = [int(input()) for _ in range(num_cup)]

if num_cup == 1:
    print(drinks[0])
else:
    dp = [0, drinks[1], drinks[0], drinks[0] + drinks[1]]
    for i in range(2, num_cup):
        curr = drinks[i]
        dp = [max(dp[0], dp[2]), max(dp[0], dp[2]) + curr, max(dp[1], dp[3]), dp[1] + curr]
    print(max(dp))