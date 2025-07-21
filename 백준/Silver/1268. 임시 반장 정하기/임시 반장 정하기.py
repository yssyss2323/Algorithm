import sys
input = sys.stdin.readline

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
friends = [[False] * n for _ in range(n)]
for i in range(n - 1):
    for j in range(i + 1, n):
        for k in range(5):
            if info[i][k] == info[j][k]:
                friends[i][j] = True
                friends[j][i] = True
ans = 0
cnt = 0
for i in range(n):
    tmp = friends[i].count(True)
    if tmp > cnt:
        ans = i
        cnt = tmp
print(ans + 1)