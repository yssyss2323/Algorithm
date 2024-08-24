a, b, d = map(int, input().split())
d = str(d)
ans = 0
prime = [False] * 2 + [True] * (b - 1)
for i in range(2, b + 1):
    if prime[i]:
        prime[i * 2::i] = [False] * len(prime[i * 2::i])
        if i >= a and d in str(i):
            ans += 1
print(ans)
