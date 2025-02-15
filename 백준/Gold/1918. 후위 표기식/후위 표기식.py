string = input()
stack = []
ans = []
for ch in string:
    if ch == '(':
        stack.append(ch)
    elif ch == ')':
        while stack:
            tmp = stack.pop()
            if tmp == '(':
                break
            else:
                ans.append(tmp)
    elif ch in '+-':
        while stack:
            tmp = stack.pop()
            if tmp in '*/+-':
                ans.append(tmp)
            else:
                stack.append(tmp)
                break
        stack.append(ch)
    elif ch in '*/':
        while stack:
            tmp = stack.pop()
            if tmp in '*/':
                ans.append(tmp)
            else:
                stack.append(tmp)
                break
        stack.append(ch)
    else:
        ans.append(ch)
while stack:
    ans.append(stack.pop())
print(*ans, sep='')