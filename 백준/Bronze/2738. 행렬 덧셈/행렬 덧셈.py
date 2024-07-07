n, m = map(int, input().split())
A, B = [], []
for _ in range(n):
    A.append(list(map(int, input().split())))
for _ in range(n):
    B.append(list(map(int, input().split())))

C = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        C[i][j] = A[i][j] + B[i][j]
for row in C:
    print(*row)