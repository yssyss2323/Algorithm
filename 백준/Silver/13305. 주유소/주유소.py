n = int(input())
roads = list(map(int, input().split()))
prices = list(map(int, input().split()))

ans = 0
curr_price = float('inf')
for i in range(n - 1):
    if prices[i] < curr_price:
        curr_price = prices[i]
    ans += roads[i] * curr_price
print(ans)