from collections import deque
for _ in range(int(input())):
    l = int(input())
    chessmap = [[-1] * l for _ in range(l)]
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    chessmap[start[0]][start[1]] = 0
    knight_xmove = [1, 1, -1, -1, 2, 2, -2, -2]
    knight_ymove = [2, -2, 2, -2, 1, -1, 1, -1]
    q = deque()
    q.append(start)
    while q:
        xnow,ynow = q.popleft()
        if [xnow,ynow] == end:
            print(chessmap[xnow][ynow])
            break
        for i in range(8):
            xnext, ynext = xnow+knight_xmove[i],ynow+knight_ymove[i]
            if 0 <= xnext < l and 0 <= ynext < l and chessmap[xnext][ynext] == -1:
                chessmap[xnext][ynext] = chessmap[xnow][ynow] + 1
                q.append([xnext,ynext])