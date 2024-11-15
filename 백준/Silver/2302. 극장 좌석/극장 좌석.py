dp = [1] * 41
dp[2] = 2
for i in range(3, 41):
    dp[i] = dp[i - 2] + dp[i - 1]

n = int(input())
m = int(input())
tmp = 0
ans = 1
for _ in range(m):
    curr = int(input())
    ans *= dp[curr - tmp - 1]
    tmp = curr
ans *= dp[n - tmp]
print(ans)