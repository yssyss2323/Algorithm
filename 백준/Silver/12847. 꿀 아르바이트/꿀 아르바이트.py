n, m = map(int, input().split())
money = list(map(int, input().split()))
check= sum(money[:m])
ans = check
for i in range(n - m):
    check += money[i+m] - money[i]
    if ans < check:
        ans = check
print(ans)