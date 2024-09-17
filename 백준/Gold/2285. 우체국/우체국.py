import sys
input = sys.stdin.readline

n = int(input())
coords = []
tot = 0
for i in range(n):
    x, a = map(int, input().split())
    tot += a
    coords.append((x, a))
coords.sort()

pfx = 0
for i in range(n):
    pfx += coords[i][1]
    if pfx >= (tot + 1) // 2:
        print(coords[i][0])
        break