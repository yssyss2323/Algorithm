n = int(input())
p_cost = list(map(int, input().split()))
m = int(input())

dp = [-1 for _ in range(m + 1)]
for i in range(n):
    if p_cost[i] < m + 1:
        dp[p_cost[i]] = i

for i in reversed(range(n)):
    tmp = p_cost[i]
    for j in range(tmp + 1, m + 1):
        dp[j] = max(dp[j], dp[j - tmp] * 10 + i)

print(max(dp))
