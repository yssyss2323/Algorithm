n = int(input())
hlist = list(map(int, input().split()))
bullets = [0] * (max(hlist) + 1)
ans = 0
for h in hlist:
    if bullets[h] > 0:
        bullets[h] -= 1
        bullets[h - 1] += 1
    else:
        ans += 1
        if h > 1:
            bullets[h - 1] += 1
print(ans)