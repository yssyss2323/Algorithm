from collections import deque

n = int(input())
numlist = deque(map(int, input().split()))
start = 1
stack = []
while numlist:
    tmp = numlist.popleft()
    if tmp == start:
        start += 1
    else:
        while stack and stack[-1] == start:
            start += 1
            stack.pop()
        stack.append(tmp)
while stack:
    tmp = stack.pop()
    if tmp == start:
        start += 1
    else:
        print('Sad')
        break
else:
    print('Nice')
