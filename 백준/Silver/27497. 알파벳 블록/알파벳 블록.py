from collections import deque
import sys

input = sys.stdin.readline

string = deque()
n = int(input())
buttonlist = []
left, right = deque(), deque()
for _ in range(n):
    buttonlist.append(input().split())

cnt = 0
for button in buttonlist[::-1]:
    if button[0] == '1':
        if cnt == 0:
            right.appendleft(button[1])
            continue
        else:
            cnt -= 1
    elif button[0] == '2':
        if cnt == 0:
            left.append(button[1])
            continue
        else:
            cnt -= 1
    else:
        cnt += 1

answer = left + right
print(''.join(left + right) if answer else 0)
