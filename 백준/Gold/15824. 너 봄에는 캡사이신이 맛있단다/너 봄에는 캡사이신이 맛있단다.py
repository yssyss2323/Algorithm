n = int(input())
hot = list(map(int, input().split()))
hot.sort()
MOD = 1000000007

pow2 = [1] * n
for i in range(1, n):
    pow2[i] = (pow2[i - 1] * 2) % MOD

ans = 0
for i in range(n):
    ans = (ans + hot[i] * (pow2[i] - pow2[n - i - 1])) % MOD
print(ans)
