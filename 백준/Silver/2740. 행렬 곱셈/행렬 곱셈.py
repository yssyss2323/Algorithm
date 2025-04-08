n, m = map(int, input().split())
alist = [tuple(map(int, input().split())) for _ in range(n)]

_, k = map(int, input().split())
blist = [tuple(map(int, input().split())) for _ in range(m)]

ans = [[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        aa = alist[i][j]
        for l in range(k):
            bb = blist[j][l]
            ans[i][l] += aa * bb

for row in ans:
    print(*row)