import sys
input = sys.stdin.readline

n, m, k, = map(int, input().split())
damage = 0
min_floor = float('inf')
for i in range(1, m + 1):
    t, r = map(int, input().split())
    damage += r
    if t < min_floor:
        min_floor = t
    if damage > k:
        print(i, min_floor)
        break
else:
    print(-1)
