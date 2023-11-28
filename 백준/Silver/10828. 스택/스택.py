from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())
stack = deque([])
printlist = []
for _ in range(N):
    tmp = sys.stdin.readline().rstrip()
    if tmp == 'pop':
        printlist.append(stack.pop() if stack else -1)
    elif tmp == 'size':
        printlist.append(len(stack))
    elif tmp == 'empty':
        printlist.append(1 if not stack else 0)
    elif tmp == 'top':
        printlist.append(stack[-1] if stack else -1)
    else:
        stack.append(int(list(tmp.split())[-1]))
for i in printlist:
    print(i)