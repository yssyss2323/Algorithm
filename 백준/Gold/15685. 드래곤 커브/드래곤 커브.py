board = [[0] * 101 for _ in range(101)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
last_points = [[(dx[i], dy[i]) for i in range(4)]]
for _ in range(10):
    curr = last_points[-1]
    tmp = []
    for i in range(4):
        tmp.append((curr[i][0] + curr[i][1], curr[i][1] - curr[i][0]))
    last_points.append(tmp)


def draw(x, y, d, g):
    if g == 0:
        board[x][y] = 1
        board[x + dx[d]][y + dy[d]] = 1
    else:
        draw(x, y, d, g - 1)
        nx, ny = x + last_points[g][d][0], y + last_points[g][d][1]
        draw(nx, ny, (d - 1) % 4, g - 1)


n = int(input())
for _ in range(n):
    x, y, d, g = map(int, input().split())
    draw(x, y, d, g)

ans = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1 and board[i][j + 1] == 1 and board[i + 1][j] == 1 and board[i + 1][j + 1] == 1:
            ans += 1
print(ans)