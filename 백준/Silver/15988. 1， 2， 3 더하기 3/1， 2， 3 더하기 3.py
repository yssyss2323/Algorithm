import sys
input = sys.stdin.readline

t = int(input())
arr = []
max_num = 0
for _ in range(t):
    tmp = int(input())
    arr.append(tmp)
    if tmp > max_num:
        max_num = tmp

if max_num == 1:
    dp = [1, 1]
elif max_num == 2:
    dp = [1, 1, 2]
elif max_num == 3:
    dp = [1, 1, 2, 4]
else:
    dp = [0] * (max_num + 1)
    dp[:4] = [1, 1, 2, 4]
    for i in range(4, max_num + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009
for i in arr:
    print(dp[i])
