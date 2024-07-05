n = int(input())
circles = []
for _ in range(n):
    x, r = map(int, input().split())
    circles.append((x-r, x+r))
circles.sort(key=lambda x: (x[0],-x[1]))

stack = []
check = []
ans = 1
for i in range(n):

    if not stack:
        stack.append(circles[i][1])
        check.append(circles[i][0])
    else:
        if circles[i][0] < stack[-1]:
            stack.append(circles[i][1])
            if check[-1] == circles[i][0]:
                check[-1] = circles[i][1]
            check.append(circles[i][0])
        else:
            while stack and circles[i][0] >= stack[-1]:
                if check.pop() == stack.pop():
                    ans += 2
                else:
                    ans += 1
            stack.append(circles[i][1])
            if check and check[-1] == circles[i][0]:
                check[-1] = circles[i][1]
            check.append(circles[i][0])
while stack:
    if check.pop() == stack.pop():
        ans += 2
    else:
        ans += 1
print(ans)