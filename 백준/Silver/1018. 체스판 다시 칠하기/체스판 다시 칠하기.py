def compare(a, b):
    tmp = [board[x][b:b + 8] for x in range(a, a + 8)]
    check = 0
    for i in range(0, 8, 2):
        for j in range(0, 8, 2):
            if tmp[i][j] == 'W':
                check += 1
            if tmp[i][j + 1] == 'B':
                check += 1
            if tmp[i + 1][j] == 'B':
                check += 1
            if tmp[i + 1][j + 1] == 'W':
                check += 1
    return min(check, 64 - check)


m, n = map(int, input().split())
board = []
for _ in range(m):
    board.append(list(input()))

answer = 64
for i in range(m - 8 + 1):
    for j in range(n - 8 + 1):
        answer = min(answer, compare(i, j))
print(answer)
