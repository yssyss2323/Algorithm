n = int(input())
MOD = 10 ** 9 + 7

def calc_pow(x):
    t = 2
    for _ in range(x):
        t = (t * t) % MOD
    return t


if n == 0:
    print(1)
else:
    nn = bin(n - 1)[2:]
    length = len(nn)
    ans = 1
    for i in range(length):
        if nn[i] == '1':
            curr = length - i - 1
            ans *= calc_pow(curr)
            ans %= MOD
    print(ans)
