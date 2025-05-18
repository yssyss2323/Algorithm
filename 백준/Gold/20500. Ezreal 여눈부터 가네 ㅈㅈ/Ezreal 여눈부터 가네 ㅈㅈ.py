n = int(input())
if n == 1:
    print(0)
else:
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = (fact[i - 1] * i)

    ans = 0
    for x in range((2 - n) % 3, n + 1, 3):
        y = n - 1 - x
        ans += fact[n - 1] // (fact[x] * fact[y])
        ans %= 1000000007
    print(ans)