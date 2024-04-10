def mul_mat(X, Y):
    t = len(X)
    Z = [[0 for _ in range(t)] for _ in range(t)]
    for i in range(t):
        for j in range(t):
            for k in range(t):
                Z[i][j] += (X[i][k] * Y[k][j])
            Z[i][j] %= 1000
    return Z

def pow(X, m):
    for _ in range(m):
        X = mul_mat(X, X)
    return X

n, b = map(int, input().split())
b_bin = bin(b)[2:]
b_pow = []
for i in range(len(b_bin)):
    if b_bin[i] == '1':
        b_pow.append(len(b_bin) - i - 1)

A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

ans = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    ans[i][i] = 1
for i in b_pow:
    ans = mul_mat(ans, pow(A, i))

for row in ans:
    print(*row)
