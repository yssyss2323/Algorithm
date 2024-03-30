n, k = map(int,input().split())
value = []
for _ in range(n):
    value.append(int(input()))
dp = [0 for _ in range(k+1)]

for i in range(n):
    tmp = value[i]
    if tmp > k:
        continue
    dp[tmp] += 1
    for j in range(tmp+1,k+1):
        dp[j] += dp[j - tmp]

print(dp[k])