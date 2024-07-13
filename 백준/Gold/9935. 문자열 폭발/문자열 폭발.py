string = input()
bomb = input()
length = len(bomb)

idx = 0
stack = []
ans = []
for ch in string:
    # print(ans, stack, idx,bomb[idx], ch)
    if ch == bomb[0]:
        stack.append(ch)
        idx = 1
        if length == 1:
            stack.pop()
            idx = 0
        continue
    if stack:
        if ch == bomb[idx]:
            stack.append(bomb[idx])
            idx += 1
            if idx == length:
                for _ in range(length):
                    stack.pop()
                idx = bomb.index(stack[-1]) + 1 if stack else 0
        else:
            ans += stack
            stack = []
            idx = 0
            ans.append(ch)
    else:
        ans.append(ch)
ans += stack
print(''.join(ans) if ans else 'FRULA')