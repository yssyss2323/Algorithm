n, m = map(int, input().split())
A = [list(map(int,input())) for _ in range(n)]
B = [list(map(int,input())) for _ in range(n)]
C = [[A[i][j] == B[i][j] for j in range(m)] for i in range(n)]

cnt = 0
for i in range(n - 2):
    for j in range(m - 2):
        if not C[i][j]:
            cnt += 1
            for a in range(3):
                for b in range(3):
                    C[i + a][j + b] = not C[i + a][j + b]
    if not C[i][m - 2] or not C[i][m - 1]:
        print(-1)
        break
else:
    for j in range(m):
        if not C[n - 2][j] or not C[n - 1][j]:
            print(-1)
            break
    else:
        print(cnt)