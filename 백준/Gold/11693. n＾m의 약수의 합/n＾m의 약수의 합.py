MOD = 1000000007

def pow_base(x):
    check = bin(x)[2:]
    length = len(check)

    arr = []
    for i in range(length):
        if check[i] == '1':
            arr.append(length - i - 1)
    return arr

def pow(x, n):
    for _ in range(n):
        x = (x ** 2) % MOD
    return x

def mod_inv(x, arr):
    ans = 1
    for i in arr:
        ans *= pow(x, i)
        ans %= MOD
    return ans

def factor(x):
    i = 2
    arr = []
    while i ** 2 <= x:
        if x % i == 0:
            cnt = 0
            while x % i == 0:
                cnt += 1
                x //= i
            arr.append((i, cnt))
        else:
            i += 1
    if x > 1:
        arr.append((x, 1))
    return arr

n, m = map(int, input().split())
mod_arr = pow_base(MOD - 2)
facs = factor(n)

ans = 1
for fac, t in facs:
    t = (t * m + 1) % (MOD - 1)
    tmp = 1
    for i in pow_base(t):
        tmp *= pow(fac, i)
        tmp %= MOD
    ans *= (tmp - 1)
    ans %= MOD
    ans *= mod_inv(fac - 1, mod_arr)
    ans %= MOD
print(ans)