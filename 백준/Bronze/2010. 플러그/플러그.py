import sys
input = sys.stdin.readline

n = int(input())
ans = 1 - n
for _ in range(n):
    ans += int(input())
print(ans)