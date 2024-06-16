import sys
import heapq

input = sys.stdin.readline
N = int(input())
heap = []
for _ in range(N):
    for i in list(map(int, input().split())):
        heapq.heappush(heap, i)
        if len(heap) > N:
            heapq.heappop(heap)

print(heapq.heappop(heap))