n = int(input())

dp = [0] + [4] * n
for i in range(1, n + 1):
    if i ** 0.5 == int(i ** 0.5):
        dp[i] = 1
    else:
        for j in range(1, int((i // 2) ** 0.5) + 1):
            if dp[i] > dp[i - j ** 2] + 1:
                dp[i] = dp[i - j ** 2] + 1
print(dp[n])