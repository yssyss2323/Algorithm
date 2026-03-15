import sys
input = sys.stdin.readline

n = int(input())
mat = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
suff_mat = [[[0] * 11 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(11):
            suff_mat[i][j][k] = suff_mat[i - 1][j][k] + suff_mat[i][j - 1][k] - suff_mat[i - 1][j - 1][k]
        suff_mat[i][j][mat[i][j]] += 1

q = int(input())
for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    ans = sum(
        1 for k in range(1, 11)
        if suff_mat[x2][y2][k] - suff_mat[x1 - 1][y2][k] - suff_mat[x2][y1 - 1][k] + suff_mat[x1 - 1][y1 - 1][k] > 0
    )
    print(ans)