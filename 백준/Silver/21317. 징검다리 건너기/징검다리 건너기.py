n = int(input())
arr = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n - 1)]
k = int(input())

def f(dp, x):
    for i in range(3, n + 1):
        if i > 3 and i == x:
            dp[i] = min(arr[i - 1][0] + dp[i - 1], arr[i - 2][1] + dp[i - 2], k + dp[i - 3])
        else:
            dp[i] = min(arr[i - 1][0] + dp[i - 1], arr[i - 2][1] + dp[i - 2])
    return dp[n]

if n == 1:
    print(0)
else:
    ans = float('inf')
    for x in range(2, n + 1):
        dp = [0] * (n + 1)
        dp[2] = arr[1][0]
        if ans > f(dp, x):
            ans = f(dp, x)
    print(ans)