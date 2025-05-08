import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [list(map(lambda x: 1 if x == 'B' else 0, input())) for _ in range(n)]

check = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        check[i][j] = check[i - 1][j] + check[i][j - 1] - check[i - 1][j - 1]
        if board[i - 1][j - 1] == (i + j) % 2:
            check[i][j] += 1

ans = k * k
for i in range(n - k + 1):
    for j in range(m - k + 1):
        tmp = check[i + k][j + k] - check[i + k][j] - check[i][j + k] + check[i][j]
        if k * k - tmp < tmp:
            tmp = k * k - tmp
        if ans > tmp:
            ans = tmp
print(ans)