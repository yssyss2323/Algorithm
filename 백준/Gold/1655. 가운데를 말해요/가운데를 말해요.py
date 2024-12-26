import heapq
import sys
input = sys.stdin.readline

n = int(input())
max_heap = [-int(input())]
min_heap = []
print(-max_heap[0])
for _ in range(n - 1):
    curr = int(input())
    if len(max_heap) == len(min_heap):
        if min_heap[0] >= curr:
            heapq.heappush(max_heap, -curr)
        else:
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
            heapq.heappush(min_heap, curr)
    else:
        if -max_heap[0] < curr:
            heapq.heappush(min_heap, curr)
        else:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
            heapq.heappush(max_heap, -curr)
    print(-max_heap[0])