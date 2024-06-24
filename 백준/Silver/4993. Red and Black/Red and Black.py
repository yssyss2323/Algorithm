dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    room = [list(input()) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if room[i][j] == '@':
                stack = [(i, j)]
                break
    ans = 1
    while stack:
        start = stack.pop()
        for i in range(4):
            next = (start[0] + dx[i], start[1] + dy[i])
            if 0 <= next[0] < h and 0 <= next[1] < w and room[next[0]][next[1]] == '.':
                stack.append(next)
                room[next[0]][next[1]] = '*'
                ans += 1
    print(ans)
