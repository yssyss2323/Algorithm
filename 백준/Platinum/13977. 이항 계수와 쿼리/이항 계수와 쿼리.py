MOD = 1000000007
check = bin(MOD - 2)[2:]
length = len(check)

arr = []
for i in range(length):
    if check[i] == '1':
        arr.append(length - i - 1)

fac = [1] * 4000001
for i in range(2, 4000001):
    fac[i] = fac[i - 1] * i % MOD
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

def ans(n, k):
    if k > n // 2:
        k = n - k

    if k == 0:
        print(1)
    else:
        ans = fac[n] * mod_inv(fac[n - k] * fac[k] % MOD)
        ans %= MOD
        print(ans)


import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    ans(n, k)