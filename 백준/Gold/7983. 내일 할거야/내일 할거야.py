import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:(x[1], -x[0]))

last = float('inf')
while arr:
    d, t = arr.pop()
    last = min(last, t)
    last -= d
print(last)
