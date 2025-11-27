n = int(input())
arr = list(map(int, input().split()))
dp = [0] + [-1] * (n - 1)

for i in range(n):
    if dp[i] == -1:
        print(-1)
        break
    for j in range(i + 1, min(i + arr[i] + 1, n)):
        if dp[j] < 0 or dp[j] > dp[i] + 1:
            dp[j] = dp[i] + 1
else:
    print(dp[-1])