r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


ans = 1
def back(arr, check):
    global ans
    x, y = arr[-1]
    flag = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in check:
            flag = False
            arr.append((nx, ny))
            check.add(board[nx][ny])
            back(arr, check)
            arr.pop()
            check.remove(board[nx][ny])
    if flag:
        if len(arr) > ans:
            ans = len(arr)

arr = [(0, 0)]
check = {board[0][0]}
back(arr, check)
print(ans)