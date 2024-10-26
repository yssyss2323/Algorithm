import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)
ans = 0
for i, j in enumerate(arr):
    if j > i:
        ans += j - i
print(ans)