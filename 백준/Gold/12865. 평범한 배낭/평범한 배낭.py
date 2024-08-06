n, k = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (k + 1)

for i in range(n):
    w, v = table[i]
    for j in range(k, w - 1, -1):
        if dp[j - w] + v > dp[j]:
            dp[j] = dp[j - w] + v

print(max(dp))