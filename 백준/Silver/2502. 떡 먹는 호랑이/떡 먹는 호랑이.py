def find_num(k):
    dp = [1, 0]
    for i in range(1, k):
        dp = [dp[1], dp[0] + dp[1]]
    return dp


d, k = map(int, input().split())
m, n = find_num(d)
tmp = k // (m + n)
for i in range(tmp, 0, -1):
    if (k - m * i) % n == 0:
        print(i)
        print((k - m * i) // n)
        break