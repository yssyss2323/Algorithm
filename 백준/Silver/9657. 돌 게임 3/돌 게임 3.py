n = int(input())
if n in (1, 3, 4):
    print('SK')
elif n == 2:
    print('CY')
else:
    dp = [0] * n
    dp[:4] = [1,0,1,1]
    for i in range(4, n):
        if 0 in (dp[i - 1], dp[i - 3], dp[i - 4]):
            dp[i] = 1
        else:
            dp[i] = 0
    print('SK' if dp[-1] else 'CY')
