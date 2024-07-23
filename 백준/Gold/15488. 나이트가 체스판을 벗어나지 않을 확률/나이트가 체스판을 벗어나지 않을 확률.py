n, x, y, k = map(int, input().split())

knight_move = [(1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,1), (-1,2)]
board = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        for t in range(8):
            di, dj = knight_move[t]
            if 0 <= i + di < n and 0 <= j + dj < n:
                board[i][j].append((i+di, j+dj))
if k == 0:
    print(1)
else:
    dp = [[0] * n for _ in range(n)]
    dp[x-1][y-1] = 1
    for _ in range(k):
        tmp_dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                tmp = board[i][j]
                for ii, jj in tmp:
                    tmp_dp[i][j] += dp[ii][jj] / 8
        dp = [[val for val in row] for row in tmp_dp]
    ans = 0
    for i in range(n):
        for j in range(n):
            ans += dp[i][j]
    print(ans)