k = int(input())

# dp[n] -> n번 눌렀을때 A,B의 개수
dp = [(1, 0)] * (k + 1)
for i in range(k):
    # 점화식 : i : (x,y) -> i + 1 : (y,x+y)
    dp[i + 1] = (dp[i][1], sum(dp[i]))
print(*dp[-1])
