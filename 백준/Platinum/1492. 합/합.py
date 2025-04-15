MOD = 1000000007
check = bin(MOD - 2)[2:]
length = len(check)

arr = []
for i in range(length):
    if check[i] == '1':
        arr.append(length - i - 1)

def square(x, n):
    for _ in range(n):
        x = (x ** 2) % MOD
    return x

def mod_inv(x):
    ans = 1
    for i in arr:
        ans *= square(x, i)
        ans %= MOD
    return ans

n, k = map(int, input().split())

coef = [[1]]
for i in range(1, k + 2):
    tmp = [1]
    for j in range(len(coef[i - 1]) - 1):
        tmp.append((coef[i - 1][j] + coef[i - 1][j + 1]) % MOD)
    tmp.append(1)
    coef.append(tmp)

n_pow = n
dp = [0] * (k + 1)
dp[0] = n
for i in range(1, k + 1):
    n_pow = n_pow * n % MOD
    tmp = n_pow
    for j in range(2, i + 2):
        if j % 2 == 0:
            tmp += coef[i + 1][j] * dp[i + 1 - j] % MOD
        else:
            tmp -= coef[i + 1][j] * dp[i + 1 - j] % MOD
        tmp %= MOD
    tmp = tmp * mod_inv(i + 1) % MOD
    dp[i] = tmp
print(dp[-1])