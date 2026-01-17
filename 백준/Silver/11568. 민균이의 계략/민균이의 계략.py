n = int(input())
arr = list(map(int, input().split()))

dp = [1]
ans = 1
for i in range(1, n):
    curr = 1
    for j in range(i):
        if arr[j] < arr[i] and curr < dp[j] + 1:
            curr = dp[j] + 1
    dp.append(curr)
    if curr > ans:
        ans = curr
print(ans)
