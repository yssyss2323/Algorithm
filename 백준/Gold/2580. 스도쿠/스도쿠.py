board = [list(map(int, input().split())) for _ in range(9)]

zeros = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zeros.append((i, j))

def sol(n):
    if n == len(zeros):
        return board

    x, y = zeros[n]

    for i in range(1, 10):
        if i in board[x]:
            continue

        if any(i == board[j][y] for j in range(9)):
            continue

        if any(board[j][k] == i for j in range(x // 3 * 3, x // 3 * 3 + 3)
               for k in range(y // 3 * 3, y // 3 * 3 + 3)):
            continue

        board[x][y] = i
        result = sol(n + 1)
        if result:
            return result
        board[x][y] = 0

for row in sol(0):
    print(*row)