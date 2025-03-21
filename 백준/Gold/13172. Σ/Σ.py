mod = 1000000007

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

def mod_square(x, mod):
    return (x * x) % mod

def mod_bin_n(x, n, mod):
    for _ in range(n):
        x = mod_square(x, mod)
    return x % mod

def get_modulo_inverse(x, num, mod):
    my_mod = bin(num)[2:]
    ans = 1
    for i in range(len(my_mod)):
        if my_mod[i] == '1':
            nn = len(my_mod) - i - 1
            ans *= mod_bin_n(x, nn, mod)
            ans %= mod
    return ans

m = int(input())
a, b = map(int, input().split())
for _ in range(m - 1):
    c, d = map(int, input().split())
    g = gcd(a, c)
    b = ((a * d + b * c) // g) % mod
    a = (a * c // g) % mod
a = get_modulo_inverse(a, mod - 2, mod)
ans = (a * b) % mod
print(ans)