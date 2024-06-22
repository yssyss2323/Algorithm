def pow(n):
    i = 2
    p = dict()
    while i ** 2 <= n:
        while n % i == 0:
            p[i] = p.get(i, 0) + 1
            n //= i
        else:
            i += 1
    else:
        if n > 1:
            p[n] = 1
    return p

def pi(n):
    if n == 1:
        return 0
    nlist = pow(n)
    for i in nlist.keys():
        n *= (i - 1)
        n //= i
    return n

def sol(n):
    ans = pi(n)
    if n % 2 == 0:
        ans += pi(n // 2)
    return ans


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(sol(n))
