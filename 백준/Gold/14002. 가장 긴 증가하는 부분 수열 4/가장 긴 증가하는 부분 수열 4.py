n = int(input())
num_list = list(map(int, input().split()))

dp = [[x] for x in num_list]
ans = dp[0]
for i in range(1, n):
    for j in range(i):
        if num_list[j] < num_list[i]:
            if len(dp[i]) <= len(dp[j]):
                dp[i] = dp[j] + [num_list[i]]
    if len(ans) < len(dp[i]):
        ans = dp[i]
print(len(ans))
print(*ans)