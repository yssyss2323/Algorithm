n = int(input())
arr = list(map(int, input().split()))
prefix_sum = [0]
tmp = 0
for i in range(n):
    tmp += arr[i]
    prefix_sum.append(tmp)

stack = []
ans = 0
for i in range(n):
    while stack and arr[stack[-1]] > arr[i]:
        h = arr[stack.pop()]
        w = prefix_sum[i] if not stack else prefix_sum[i] - prefix_sum[stack[-1] + 1]
        if h * w > ans:
            ans = h * w
    stack.append(i)

while stack:
    h = arr[stack.pop()]
    w = prefix_sum[n] if not stack else prefix_sum[n] - prefix_sum[stack[-1] + 1]
    if h * w > ans:
        ans = h * w

print(ans)