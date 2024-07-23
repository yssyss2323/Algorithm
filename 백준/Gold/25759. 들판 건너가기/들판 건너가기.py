n = int(input())
beauty = list(map(int, input().split()))
end = max(beauty) + 1

dp = [-float('inf')] * end
dp[beauty[0]] = 0

for i in range(1, n):
    curr = beauty[i]
    # print(i, curr)
    for j in range(1, end):
        if dp[j] >= 0:
            dp[curr] = max(dp[curr], dp[j] + (curr - j) ** 2)
            # print(dp)
print(max(dp))