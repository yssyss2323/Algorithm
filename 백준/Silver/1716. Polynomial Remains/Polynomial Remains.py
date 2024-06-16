import sys
input = sys.stdin.readline

while True:
    n, k = map(int, input().split())
    if n == -1 and k == -1:
        break

    coeff = list(map(int, input().split()))
    if k == 0:
        print(0)
    elif k > n:
        print(*coeff)
    else:
        coeff += [0] * k
        c = coeff[:k]
        for i in range(k, n + 1, k):
            for j in range(k):
                c[j] += coeff[i + j] * (-1) ** (i // k)
        print(*c)
