n, m = map(int, input().split())
my_table = [[True if i else False for i in list(map(int, input().split()))] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs1(table):
    w, h = len(table[0]), len(table)
    visited = [[table[i][j] for j in range(w)] for i in range(h)]
    next_table = [[table[i][j] for j in range(w)] for i in range(h)]
    visited[0][0] = True
    stack = [(0, 0)]
    while stack:
        curr = stack.pop()
        for i in range(4):
            nexth, nextw = curr[0] + dx[i], curr[1] + dy[i]
            if 0 <= nexth < h and 0 <= nextw < w and not table[nexth][nextw]:
                table[nexth][nextw] = True
                stack.append((nexth, nextw))
                for j in range(4):
                    checkx, checky = nexth + dx[j], nextw + dy[j]
                    if 0 <= checkx < h and 0 <= checky < w and table[checkx][checky]:
                        next_table[checkx][checky] = False
    all_over = True
    for i in range(h):
        for j in range(w):
            if next_table[i][j]:
                all_over = False
                break
    return next_table, all_over


time = 0
while True:
    time += 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if my_table[i][j]:
                cnt += 1

    my_table, over = dfs1(my_table)
    if over:
        print(time)
        print(cnt)
        break
