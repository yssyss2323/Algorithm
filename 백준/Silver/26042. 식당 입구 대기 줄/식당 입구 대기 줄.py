from collections import deque
import sys
input = sys.stdin.readline

q = deque()
maxnum = -1
curr = 0
lastnum = float('inf')
for _ in range(int(input())):
    order = list(map(int, input().split()))
    if order[0] == 1:
        q.append(order[1])
        curr += 1
        if curr > maxnum:
            maxnum = curr
            lastnum = order[1]
        elif curr == maxnum:
            if lastnum > order[1]:
                lastnum = order[1]
    else:
        curr -= 1
        q.popleft()
print(maxnum, lastnum)