def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

def pow(x, n, mod):
    for _ in range(n):
        x = (x * x) % mod
    return x

def pi(n):
    nn = n
    i = 2
    arr = []
    while i * i <= nn:
        if nn % i == 0:
            arr.append(i)
            while nn % i == 0:
                nn //= i
        else:
            i += 1
    if nn > 1:
        arr.append(nn)
    for i in arr:
        n *= (i - 1)
        n //= i
    return n

def get_inv(n, mod):
    m = pi(mod)
    check = bin(m - 1)[2:]
    length = len(check)

    ans = 1
    for i in range(length):
        if check[i] == '1':
            ans *= pow(n, length - i - 1, mod)
            ans %= mod
    return ans


n, a = map(int, input().split())
if gcd(n, a) > 1:
    print(n - a, -1)
else:
    print(n - a, get_inv(a, n))
