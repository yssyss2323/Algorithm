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

if k == 0:
    print(1)
else:
    n1 = n
    n2 = 1
    for i in range(2, k + 1):
        n1 *= (n - i + 1)
        n1 %= MOD
        n2 *= i
        n2 %= MOD

    ans = n1 * mod_inv(n2)
    ans %= MOD
    print(ans)