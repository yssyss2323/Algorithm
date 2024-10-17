n = int(input())

dp = [0] * (n + 1)
anslist = [[], [1]]
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    tmp = anslist[i - 1] + [i]
    if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
        dp[i] = dp[i // 2] + 1
        tmp = anslist[i // 2] + [i]
    if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
        dp[i] = dp[i // 3] + 1
        tmp = anslist[i // 3] + [i]
    anslist.append(tmp)
anslist[-1].reverse()
print(dp[-1])
print(*anslist[-1])