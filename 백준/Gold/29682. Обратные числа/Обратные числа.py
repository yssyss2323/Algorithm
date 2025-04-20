def pow_base(x):
    check = bin(x)[2:]
    length = len(check)

    arr = []
    for i in range(length):
        if check[i] == '1':
            arr.append(length - i - 1)
    return arr

def pow(x, n, mod):
    for _ in range(n):
        x = (x ** 2) % mod
    return x

def mod_inv(x, arr, mod):
    ans = 1
    for i in arr:
        ans *= pow(x, i, mod)
        ans %= mod
    return ans


a, m = map(int, input().split())
print(mod_inv(a, pow_base(m - 2), m))
