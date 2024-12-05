n = input()
length = len(n)
dp = [0] * (length + 1)
dp[0] = 1

for i in range(1, length + 1):
    if n[i - 1] != '0':
        dp[i] += dp[i - 1]
    if i > 1 and (n[i - 2] == '1' or (n[i - 2] == '2' and n[i - 1] in '0123456')):
        dp[i] += dp[i - 2]
    dp[i] %= 1000000

print(dp[length])