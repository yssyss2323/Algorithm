import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    t, p = map(int, input().split())
    arr.append((t, p))

dp = [0] * (n + 2)
for i in range(n, 0, -1):
    if i + arr[i - 1][0] <= n + 1:
        dp[i] = max(dp[i + 1], dp[i + arr[i - 1][0]] + arr[i - 1][1])
    else:
        dp[i] = dp[i + 1]

print(dp[1])
