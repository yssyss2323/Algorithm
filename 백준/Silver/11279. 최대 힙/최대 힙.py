import heapq
import sys

input = lambda:sys.stdin.readline().rstrip()
heap_max = []
N = int(input())
for _ in range(N):
    tmp = int(input())
    if tmp:
        heapq.heappush(heap_max,-tmp)
    else:
        if heap_max:
            print(-heapq.heappop(heap_max))
        else:
            print(0)