import sys
sys.setrecursionlimit(10 ** 6)
input = lambda: sys.stdin.readline().rstrip()

answerlist = {-1: 0, 0: 0, 1: 0}
def counting(x, y, n):
    check = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != paper[i][j]:
                for k in range(3):
                    for l in range(3):
                        counting(x + k * n // 3, y + l * n // 3, n // 3)
                return
    answerlist[check] += 1

n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))
counting(0, 0, n)
print(answerlist[-1])
print(answerlist[0])
print(answerlist[1])