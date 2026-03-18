c, k = map(int, input().split())
if k == 0:
    print(c)
else:
    k = 10 ** k
    ans = c - c % k
    ans += k if c % k >= k // 2 else 0
    print(ans)