def comb(n, m, memo={}):
    if m == 0 or m == n:
        return 1
    if (n, m) in memo:
        return memo[(n, m)]
    memo[(n, m)] = comb(n - 1, m, memo) + comb(n - 1, m - 1, memo)
    return memo[(n, m)]

n, m = map(int, input().split())
print(comb(n, m))