k = int(input())

# dp[n] -> n번 눌렀을때 A,B의 개수
dp = [(1, 0)]
for _ in range(k):
    # 점화식 : i : (x,y) -> i + 1 : (y,x+y)
    dp.append((dp[-1][1], sum(dp[-1])))
print(*dp[-1])