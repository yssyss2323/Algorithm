n = int(input())

if n % 2:
    print(0)
else:
    if n == 2:
        print(3)
    elif n == 4:
        print(11)
    else:
        dp = [0, 3, 11] + [0] * (n // 2 - 2)
        tmp = 0
        for i in range(3, n // 2 + 1):
            tmp += dp[i - 2]
            dp[i] = dp[i - 1] * 3 + tmp * 2 + 2
        print(dp[-1])
