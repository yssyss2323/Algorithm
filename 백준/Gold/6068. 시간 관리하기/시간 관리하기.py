import sys
input = sys.stdin.readline

final = 0
n = int(input())
arr = []
for _ in range(n):
    t, s = map(int, input().split())
    if s > final:
        final = s
    arr.append((t, s))
arr.sort(key=lambda x: (-x[1], x[0]))

for i in range(n):
    final = min(final, arr[i][1]) - arr[i][0]
    if final < 0:
        print(-1)
        break
else:
    print(final)