from collections import deque
import sys

input = sys.stdin.readline

string = deque()
n = int(input())
tmp = []
for _ in range(n):
    button = input().split()
    if button[0] == '1':
        string.append(button[1])
        tmp.append(True)
    elif button[0] == '2':
        string.appendleft(button[1])
        tmp.append(False)
    else:
        if tmp:
            if tmp.pop():
                string.pop()
            else:
                string.popleft()

print(''.join(string) if string else 0)
