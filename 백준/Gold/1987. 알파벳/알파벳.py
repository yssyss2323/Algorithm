r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

stack = set()
stack.add((0, 0, board[0][0]))

ans = 1
while stack:
    x, y, s = stack.pop()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in s:
            ns = s + board[nx][ny]
            stack.add((nx, ny, ns))
            if len(ns) > ans:
                ans = len(ns)
    if ans == 26:
        print(26)
        break
else:
    print(ans)