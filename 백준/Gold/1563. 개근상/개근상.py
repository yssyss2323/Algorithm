n = int(input())
dp = [1,1,0,1,0,0]
for _ in range(n - 1):
    tmp = [x % 10**6 for x in dp]
    dp[0] = tmp[0] + tmp[1] + tmp[2]
    dp[1] = tmp[0]
    dp[2] = tmp[1]
    dp[3] = tmp[0] + tmp[1] + tmp[2] + tmp[3] + tmp[4] + tmp[5]
    dp[4] = tmp[3]
    dp[5] = tmp[4]
print(sum(dp) % 10**6)