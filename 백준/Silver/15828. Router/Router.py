from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
buffer = deque()
while True:
    tmp = int(input())

    if tmp == -1:  # 종료입력
        break

    if tmp != 0:
        if len(buffer) < N:  # 버퍼가 가득차지 않은 경우에 입력을 받는다
            buffer.append(tmp)
    else:
        buffer.popleft()

if buffer:
    print(*buffer)
else:
    print("empty")
