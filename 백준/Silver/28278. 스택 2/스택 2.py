import sys

input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    order = input()
    tmp = order[0]
    if tmp == '1':
        stack.append(int(order[2:]))
    elif tmp == '2':
        print(stack.pop() if stack else -1)
    elif tmp == '3':
        print(len(stack))
    elif tmp == '4':
        print(0 if stack else 1)
    else:
        print(stack[-1] if stack else -1)
