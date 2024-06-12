from collections import deque

S = input()
answer = ''
stack1 = []
stack2 = deque([])

for i in range(len(S)):
    ch = S[i]
    unit = ''
    if ch == '<':
        if stack2:
            unit = ''.join(stack2)
            answer += unit
            stack2 = deque([])
        stack1.append(ch)
        continue

    if stack1:
        stack1.append(ch)
        if ch == '>':
            unit = ''.join(stack1)
            answer += unit
            stack1 = []
    else:
        if ch == ' ':
            unit = ''.join(stack2) + ch
            answer += unit
            stack2 = deque([])
        elif i == len(S) - 1:
            stack2.appendleft(ch)
            unit = ''.join(stack2)
            answer += unit
            stack2 = deque([])
        else:
            stack2.appendleft(ch)

print(answer)