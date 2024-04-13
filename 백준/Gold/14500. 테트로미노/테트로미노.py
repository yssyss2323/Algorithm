import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int,input().split())
paper = []
for _ in range(n):
    row = [-float('inf')] * 2 + list(map(int,input().split())) + [-float('inf')] * 3
    paper.append(row)
for _ in range(3):
    paper.append([-float('inf')] * (m + 4))

answer = 0
for i in range(n):
    for j in range(2,m+2):
        answer = max(answer,
                     paper[i][j]+paper[i+1][j]+paper[i+2][j]+paper[i+3][j],
                     paper[i][j] + paper[i + 1][j] + paper[i + 2][j] + paper[i + 2][j+1],
                     paper[i][j] + paper[i + 1][j] + paper[i + 2][j] + paper[i + 2][j - 1],
                     paper[i][j] + paper[i + 1][j] + paper[i + 1][j+1] + paper[i + 2][j + 1],
                     paper[i][j] + paper[i + 1][j] + paper[i + 1][j-1] + paper[i + 2][j - 1],
                     paper[i][j] + paper[i + 1][j] + paper[i + 1][j-1] + paper[i + 1][j + 1],
                     paper[i][j] + paper[i + 1][j] + paper[i + 1][j-1] + paper[i + 2][j],
                     paper[i][j] + paper[i + 1][j] + paper[i + 1][j+1] + paper[i + 2][j],
                     paper[i][j] + paper[i + 1][j] + paper[i + 1][j-1] + paper[i + 1][j - 2],
                     paper[i][j] + paper[i + 1][j] + paper[i + 1][j + 1] + paper[i + 1][j + 2],
                     paper[i][j] + paper[i][j+1] + paper[i + 1][j] + paper[i + 1][j +1],
                     paper[i][j] + paper[i][j + 1] + paper[i + 1][j] + paper[i + 2][j],
                     paper[i][j] + paper[i][j + 1] + paper[i + 1][j+1] + paper[i + 2][j+1],
                     paper[i][j] + paper[i][j + 1] + paper[i + 1][j] + paper[i + 1][j-1],
                     paper[i][j] + paper[i][j + 1] + paper[i + 1][j+1] + paper[i + 1][j + 2],
                     paper[i][j] + paper[i][j + 1] + paper[i][j + 2] + paper[i + 1][j],
                     paper[i][j] + paper[i][j + 1] + paper[i][j + 2] + paper[i + 1][j+2],
                     paper[i][j] + paper[i][j + 1] + paper[i][j + 2] + paper[i + 1][j+1],
                     paper[i][j] + paper[i][j + 1] + paper[i][j + 2] + paper[i][j+3])
print(answer)