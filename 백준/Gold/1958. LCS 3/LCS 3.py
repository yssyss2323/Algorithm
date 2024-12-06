str1 = input()
str2 = input()
str3 = input()


dp = [[[0] * (len(str1) + 1) for _ in range(len(str2) + 1)] for _ in range(len(str3) + 1)]
for i in range(1, len(str1) + 1):
    ch1 = str1[i - 1]
    for j in range(1, len(str2) + 1):
        ch2 = str2[j - 1]
        for k in range(1, len(str3) + 1):
            ch3 = str3[k - 1]
            if ch1 == ch2 == ch3:
                dp[k][j][i] = dp[k - 1][j - 1][i - 1] + 1
            else:
                dp[k][j][i] = max(dp[k - 1][j][i], dp[k][j - 1][i], dp[k][j][i - 1])
print(dp[-1][-1][-1])