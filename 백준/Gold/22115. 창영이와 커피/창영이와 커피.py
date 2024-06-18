n, k = map(int, input().split())
caffein = [x for x in list(map(int, input().split())) if x <= k]

dp = [0] + [float('inf')] * k
for c in caffein:
    for j in range(k, c - 1, -1):
        if dp[j - c] != float('inf'):
            dp[j] = min(dp[j], dp[j - c] + 1)

if dp[-1] == float('inf'):
    print(-1)
else:
    print(dp[-1])
