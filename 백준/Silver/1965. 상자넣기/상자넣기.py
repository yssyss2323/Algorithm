n = int(input())
sizes = list(map(int, input().split()))

dp = [1] * n
ans = 0
for i in range(1, n):
    size = sizes[i]

    for j in range(i):
        if size > sizes[j]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    if ans < dp[i]:
        ans = dp[i]

print(ans)