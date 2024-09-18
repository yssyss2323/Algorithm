import sys
input = sys.stdin.readline

n = int(input())
coords = []
tot = 0
for _ in range(n):
    x, a = map(int, input().split())
    tot += a
    coords.append((x, a))
coords.sort()

tmp = 0
for i in range(n):
    tmp += coords[i][1]
    if tmp >= (tot + 1) // 2:
        print(coords[i][0])
        break