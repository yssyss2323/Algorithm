n = int(input())
cost = list(map(int, input().split()))
cost.sort()


ans = sum(cost[n // 2:]) * 2
if n % 2:
    ans -= cost[n // 2]
print(ans)