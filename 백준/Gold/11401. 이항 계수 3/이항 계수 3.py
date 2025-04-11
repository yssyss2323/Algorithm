MOD = 1000000007
check = bin(MOD - 2)[2:]
length = len(check)

arr = []
for i in range(length):
    if check[i] == '1':
        arr.append(length - i - 1)

def pow(x, n):
    for _ in range(n):
        x = (x ** 2) % MOD
    return x

def mod_inv(x):
    ans = 1
    for i in arr:
        ans *= pow(x, i)
        ans %= MOD
    return ans

n, k = map(int, input().split())
if k > n // 2:
    k = n - k

ans = 1
for i in range(k):
    ans *= (n - i)
    ans %= MOD
    ans *= mod_inv(i + 1)
    ans %= MOD
print(ans)