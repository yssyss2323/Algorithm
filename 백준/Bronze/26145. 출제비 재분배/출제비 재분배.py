import sys
input = sys.stdin.readline

n, m = map(int, input().split())
slist = list(map(int, input().split())) + [0] * m

for i in range(n):
    tlist = list(map(int, input().split()))
    for j in range(n + m):
        slist[j] += tlist[j]
        slist[i] -= tlist[j]

print(*slist)