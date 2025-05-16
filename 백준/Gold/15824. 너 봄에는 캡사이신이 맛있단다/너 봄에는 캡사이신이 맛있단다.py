n = int(input())
hot = list(map(int, input().split()))
hot.sort()
MOD = 1000000007
ans = 0
for i in range(1, n):
    for j in range(i):
        ans += ((hot[i] - hot[j]) * 2 ** (i - j - 1)) % MOD
        ans %= MOD
print(ans)
