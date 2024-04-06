N = int(input())
picture = []
for _ in range(N):
    picture.append(list(input()))
stack1, stack2 = [], []
visited1 = [[False for _ in range(N)] for _ in range(N)]
visited2 = [[False for _ in range(N)] for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 적록색약 x
def dfs1(x, y):
    visited1[x][y] = True
    stack1.append([x, y])
    while stack1:
        now = stack1.pop()
        for i in range(4):
            x_next = now[0] + dx[i]
            y_next = now[1] + dy[i]
            if 0 <= x_next < N and 0 <= y_next < N and not visited1[x_next][y_next]:
                if picture[x][y] == picture[x_next][y_next]:
                    stack1.append([x_next, y_next])
                    visited1[x_next][y_next] = True

# 적록색약 o
def dfs2(x, y):
    visited2[x][y] = True
    stack2.append([x, y])
    while stack2:
        now = stack2.pop()
        for i in range(4):
            x_next = now[0] + dx[i]
            y_next = now[1] + dy[i]
            if 0 <= x_next < N and 0 <= y_next < N and not visited2[x_next][y_next]:
                if picture[x][y] in "RG":
                    if picture[x_next][y_next] in "RG":
                        stack2.append([x_next, y_next])
                        visited2[x_next][y_next] = True
                else:
                    if picture[x_next][y_next] == "B":
                        stack2.append([x_next, y_next])
                        visited2[x_next][y_next] = True

answer1, answer2 = 0, 0
for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            dfs1(i, j)
            answer1 += 1
        if not visited2[i][j]:
            dfs2(i, j)
            answer2 += 1
print(answer1, answer2)
