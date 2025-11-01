n = int(input())
mod = 10 ** 9 + 7
ans = 1
for i in range(4, n + 1, 2):
    ans *= (i - 1)
    ans %= mod
print(ans)
