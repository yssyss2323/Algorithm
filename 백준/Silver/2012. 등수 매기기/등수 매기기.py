import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

ans = 0
for i, j in enumerate(arr):
    ans += abs((i + 1) - j)
print(ans)