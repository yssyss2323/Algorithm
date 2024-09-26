import sys
input = sys.stdin.readline

n, k = map(int, input().split())
values = [int(input()) for _ in range(n)]
values.sort()

dp = [float('inf')] * (k + 1)
for val in values:
    for i in range(val, k + 1):
        if i % val == 0:
            dp[i] = min(dp[i - val] + 1, i // val)
        else:
            dp[i] = min(dp[i - val] + 1, dp[i])

if dp[-1] == float('inf'):
    print(-1)
else:
    print(dp[-1])