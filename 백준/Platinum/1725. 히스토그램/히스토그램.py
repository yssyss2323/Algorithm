import sys
input = sys.stdin.readline

n = int(input())
heights = [int(input()) for _ in range(n)]

stack = []
ans = 0
for i in range(n):
    while stack and heights[stack[-1]] > heights[i]:
        h = heights[stack.pop()]
        w = i if not stack else i - stack[-1] - 1
        if h * w > ans:
            ans = h * w
    stack.append(i)

while stack:
    h = heights[stack.pop()]
    w = n if not stack else n - stack[-1] - 1
    if h * w > ans:
        ans = h * w

print(ans)