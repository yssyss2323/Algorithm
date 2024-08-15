board = [[-1] * 1001 for _ in range(10001)]
n = int(input())
for x in range(n):
    a, b, d1, d2 = map(int, input().split())
    for i in range(a, a + d1):
        for j in range(b, b + d2):
            board[i][j] = x

ans = [0] * n
for row in board:
    for i in range(n):
        ans[i] += row.count(i)
print(*ans, sep='\n')
