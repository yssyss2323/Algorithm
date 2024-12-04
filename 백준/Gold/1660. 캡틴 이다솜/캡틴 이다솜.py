def f(x):
    return x * (x + 1) * (x + 2) // 6

n = int(input())
x = int((6 * n) ** (1/3) - 1)
if f(x + 1) <= n:
    x += 1

check = []
for i in range(1, x + 1):
    check.append(f(i))

dp = [float('inf')] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    for j in check:
        if j <= i:
            if dp[i] > dp[i - j] + 1:
                dp[i] = dp[i - j] + 1
        else:
            break
print(dp[-1])