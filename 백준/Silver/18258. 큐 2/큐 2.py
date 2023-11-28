import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque
q = deque()
n = int(input())
for _ in range(n):
    order = input()
    if order == 'pop':
        print(q.popleft() if q else -1)
    elif order == 'size':
        print(len(q))
    elif order == 'empty':
        print(1 if not q else 0)
    elif order == 'front':
        print(q[0] if q else -1)
    elif order == 'back':
        print(q[-1] if q else -1)
    else: # input이 push X인 경우
        order,num = order.split()
        q.append(num)