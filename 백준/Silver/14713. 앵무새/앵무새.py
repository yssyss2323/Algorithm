from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
qlist = [deque(input().split()) for _ in range(N)]

L = input().split()
for word in L:
    for i in range(N):
        if qlist[i] and qlist[i][0] == word:
            qlist[i].popleft()  # 큐의 popleft는 O(1)
            break
    else:
        print("Impossible")
        break
else:
    for q in qlist:
        if q:
            print("Impossible")
            break
    else:
        print("Possible")
