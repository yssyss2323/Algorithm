import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

num_paint = 0
biggest = 0
for i in range(n):
    for j in range(m):
        if paper[i][j] == 1:
            num_paint += 1
            stack = [(i, j)]
            paper[i][j] = 2
            tmp = 1
            while stack:
                current = stack.pop()
                for k in range(4):
                    xnext, ynext = current[0] + dx[k], current[1] + dy[k]
                    if 0 <= xnext < n and 0 <= ynext < m and paper[xnext][ynext] == 1:
                        paper[xnext][ynext] = 2
                        tmp += 1
                        stack.append((xnext, ynext))
            if tmp > biggest:
                biggest = tmp
print(num_paint)
print(biggest)