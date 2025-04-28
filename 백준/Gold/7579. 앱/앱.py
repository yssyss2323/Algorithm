n, m = map(int, input().split())
mlist = list(map(int, input().split()))
clist = list(map(int, input().split()))
cclist = []

dp = [0] + [float('inf')] * 10000
for i in range(n):
    if clist[i] == 0:
        m -= mlist[i]
        cclist.append(float('inf'))
    else:
        cclist.append(clist[i])

for i in range(n):
    c = cclist[i]
    if c == float('inf'):
        continue
    for j in range(10000, 0, -1):
        if j - c < 0:
            continue
        if dp[j - c] != float('inf'):
            if dp[j] == float('inf'):
                dp[j] = dp[j - c] + mlist[i]
            elif dp[j] < dp[j - c] + mlist[i]:
                dp[j] = dp[j - c] + mlist[i]

for i in range(10001):
    if dp[i] != float('inf') and dp[i] >= m:
        print(i)
        break
