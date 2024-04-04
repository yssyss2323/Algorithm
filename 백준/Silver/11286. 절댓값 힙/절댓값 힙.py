import heapq
import sys

input = lambda:sys.stdin.readline().rstrip()
heap_abs = []
N = int(input())
for _ in range(N):
    tmp = int(input())
    if tmp > 0:
        heapq.heappush(heap_abs,tmp)
    elif tmp < 0:
        heapq.heappush(heap_abs, -tmp - 0.5)
    else:
        if heap_abs:
            tmp2 = heapq.heappop(heap_abs)
            if tmp2 == int(tmp2):
                print(tmp2)
            else:
                print(int(-tmp2 - 0.5))
        else:
            print(0)