n = int(input())
p_cost = list(map(int, input().split()))
m = int(input())

dp = ['' for _ in range(m + 1)]
for i in range(n):
    if 0 <= p_cost[i] < m + 1:
        dp[p_cost[i]] = str(i)

for i in range(1, m + 1):
    for j in range(n):
        if i >= p_cost[j] and dp[i - p_cost[j]]:
            tmp = dp[i - p_cost[j]]
            for k in range(len(tmp)):
                if int(tmp[k]) <= j:
                    tmp = tmp[:k] + str(j) + tmp[k:]
                    break
            else:
                tmp = tmp + str(j)
            dp[i] = str(max(int(dp[i]), int(tmp))) if dp[i] else tmp

answer = 0
for i in dp:
    if i:
        tmp = int(i)
        if tmp > answer:
            answer = tmp
print(answer)
