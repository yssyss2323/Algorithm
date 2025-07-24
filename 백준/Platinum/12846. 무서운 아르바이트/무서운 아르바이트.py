n = int(input())
arr = list(map(int, input().split()))
stack = []
ans = 0
for i in range(n):
    while stack and arr[stack[-1]] > arr[i]:
        h = arr[stack.pop()]
        w = i if not stack else i - stack[-1] - 1
        if h * w > ans:
            ans = h * w
    stack.append(i)

while stack:
    h = arr[stack.pop()]
    w = n if not stack else n - stack[-1] - 1
    if h * w > ans:
        ans = h * w

print(ans)