import heapq
import sys

input = lambda:sys.stdin.readline().rstrip()
heap_min = []
N = int(input())
for _ in range(N):
    tmp = int(input())
    if tmp:
        heapq.heappush(heap_min,tmp)
    else:
        if heap_min:
            print(heapq.heappop(heap_min))
        else:
            print(0)