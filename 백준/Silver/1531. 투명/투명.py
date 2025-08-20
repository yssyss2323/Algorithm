n, m = map(int, input().split())
board = [[0] * 100 for _ in range(100)]
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1 - 1, x2):
        for j in range(y1 - 1, y2):
            board[i][j] += 1
ans = 0
for row in board:
    ans += sum([1 for i in row if i > m])
print(ans)
