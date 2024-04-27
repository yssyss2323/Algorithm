def comb(a, b):
    if b == 0:
        return 1
    elif a == b:
        return 1
    else:
        return comb(a - 1, b - 1) + comb(a - 1, b)

N, K = map(int, input().split())
print(comb(N, K))
