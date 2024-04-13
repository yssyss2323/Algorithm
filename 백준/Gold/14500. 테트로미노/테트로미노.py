import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
paper = []
for _ in range(n):
    row = [-float('inf')] * 2 + list(map(int, input().split())) + [-float('inf')] * 3
    paper.append(row)
for _ in range(3):
    paper.append([-float('inf')] * (m + 4))

answer = 0
for i in range(n):
    for j in range(2, m + 2):
        tmp11 = max(paper[i + 2][j + 1], paper[i + 2][j - 1], paper[i + 3][j])
        tmp12 = max(paper[i + 2][j + 1], paper[i + 1][j + 2], paper[i + 2][j])
        tmp13 = max(paper[i + 1][j - 2], paper[i + 2][j - 1], paper[i + 1][j + 1], paper[i + 2][j])
        tmp1 = max(paper[i + 2][j] + tmp11, paper[i + 1][j + 1] + tmp12, paper[i + 1][j - 1] + tmp13)
        tmp21 = max(paper[i + 1][j + 1], paper[i + 2][j], paper[i + 1][j - 1])
        tmp22 = max(paper[i + 2][j + 1], paper[i + 1][j + 2])
        tmp23 = max(paper[i + 1][j], paper[i + 1][j + 2], paper[i + 1][j + 1], paper[i][j + 3])
        tmp2 = max(paper[i + 1][j] + tmp21, paper[i + 1][j + 1] + tmp22, paper[i][j + 2] + tmp23)
        answer = max(answer, paper[i][j] + paper[i + 1][j] + tmp1, paper[i][j] + paper[i][j + 1] + tmp2)
print(answer)
