string1 = input()
string2 = input()

dp = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]
for i in range(1, len(string1) + 1):
    ch1 = string1[i - 1]
    for j in range(1, len(string2) + 1):
        ch2 = string2[j - 1]
        if ch1 == ch2:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[-1][-1])