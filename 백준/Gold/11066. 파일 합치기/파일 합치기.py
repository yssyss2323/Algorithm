import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    arr = list(map(int, input().split()))

    dp = [[float('inf')] * k for _ in range(k)]
    suf_sum = [sum(arr[:i]) for i in range(k + 1)]

    for gap in range(k):
        for i in range(k - gap):
            if gap == 0:
                dp[i][i + gap] = 0
            elif gap == 1:
                dp[i][i + gap] = arr[i] + arr[i + gap]
            else:
                dp[i][i + gap] = min(dp[i][i + gap - 1] * 2 + arr[i + gap], arr[i] + dp[i + 1][i + gap] * 2)
                for j in range(1, gap + 1):
                    curr = dp[i][i + gap - j] + dp[i + gap - j + 1][i + gap] + suf_sum[i + gap + 1] - suf_sum[i]
                    if dp[i][i + gap] > curr:
                        dp[i][i + gap] = curr
    print(dp[0][-1])