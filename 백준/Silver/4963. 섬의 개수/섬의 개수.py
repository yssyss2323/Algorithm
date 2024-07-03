dx = [1, 1, 1, -1, -1, -1, 0, 0]
dy = [1, 0, -1, 1, 0, -1, 1, -1]

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break

    my_map = [list(map(int, input().split())) for _ in range(h)]

    ans = 0
    for i in range(h):
        for j in range(w):
            if my_map[i][j] == 1:
                ans += 1
                stack = [(i, j)]
                while stack:
                    current = stack.pop()
                    for k in range(8):
                        xnext, ynext = current[0] + dx[k], current[1] + dy[k]
                        if 0 <= xnext < h and 0 <= ynext < w and my_map[xnext][ynext] == 1:
                            my_map[xnext][ynext] = 2
                            stack.append((xnext, ynext))
    print(ans)
