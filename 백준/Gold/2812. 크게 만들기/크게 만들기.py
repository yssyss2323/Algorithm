n, k = map(int, input().split())
num = input()
stack = []
cnt = 0
for i in range(n):
    curr = int(num[i])
    if not stack:
        stack.append(curr)
    else:
        while cnt < k and stack and stack[-1] < curr:
            stack.pop()
            cnt += 1
        stack.append(curr)
while len(stack) > n - k:
    stack.pop()
print(*stack, sep='')